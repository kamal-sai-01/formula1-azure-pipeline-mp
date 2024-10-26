# Formula 1 Data Ingestion and Transformation Pipeline

## Project Overview

This project leverages Azure Databricks, Azure Data Lake Storage Gen2, and Azure Data Factory for orchestration, storage, and automation of the ingestion and transformation of Formula 1 data. The pipeline is designed to trigger automatically after data is uploaded for each race held in the respective week, ensuring that the latest data is ingested and processed seamlessly.

## Project Description

The project includes:
- Databricks notebooks containing the code for all stages and tasks of the pipeline.
- Configuration files for all Azure Data Factory resources like pipelines, datasets, linked services, and triggers.
- Raw data for the pipeline, organized by ingestion date.

The pipeline is structured to perform the following steps:

1. **File Check**: Verifies whether new data files are uploaded to the target folder.
2. **Ingest Raw Data**: Ingests the raw data and transfers it into the processing environment.
3. **Transform Data**: Applies necessary transformations to prepare the data for analysis.

**Note**: Follow the flow chart in the README.md file inside the `adf_resources` folder for a better understanding of the pipeline.

All stages and tasks within the pipeline are implemented using PySpark within Azure Databricks notebooks.
