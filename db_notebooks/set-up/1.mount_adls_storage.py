# Databricks notebook source
dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope = 'formula1-scope')

# COMMAND ----------

def mount_container(storage_account,container_name):
  # Get Secrets from Azure Key Vault
  client_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-client-id')
  tenant_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-tenant-id')
  client_secret = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-secret')

  # Get Spark config
  configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
  
  # check if the mount already exists
  if any(mount.mountPoint == f"/mnt/formula1dl/{container_name}" for mount in dbutils.fs.mounts()):
    dbutils.fs.unmount(f"/mnt/formula1dl/{container_name}")
  
  #mount the storage container
  dbutils.fs.mount(
    source=f"abfss://{container_name}@{storage_account}.dfs.core.windows.net/",
    mount_point=f"/mnt/formula1dl/{container_name}",
    extra_configs = configs)

  # Display container once mounted
  display(dbutils.fs.mounts())

# COMMAND ----------

mount_container("dbcourseform1dl","raw")

# COMMAND ----------

mount_container("dbcourseform1dl","processed")

# COMMAND ----------

mount_container("dbcourseform1dl","presentation")

# COMMAND ----------

# to unmount
# dbutils.fs.unmount("/mnt/formula1dl/demo")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/raw")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/processed")

# COMMAND ----------

dbutils.fs.ls("/mnt/formula1dl/presentation")