from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.entity.artifact_entity import DataValidationArtifact
import os

import sys
if __name__=='__main__':
  try:
    import os

    # print("Current Working Directory:", os.getcwd())
    # print("Schema Exists:", os.path.exists("data_schema/schema.yml"))
    trainingpipelineconfig=TrainingPipelineConfig()
    dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
    data_ingestion=DataIngestion(dataingestionconfig)
    logging.info("Initiate Data Ingestion")
    dataingestionartifact=data_ingestion.initiate_data_ingestion()
    logging.info("data Initiation Completed")
    print(dataingestionartifact)
    data_validation_config=DataValidationConfig(trainingpipelineconfig)
    data_validation=DataValidation(dataingestionartifact,data_validation_config)
    logging.info("Initiate the data validation")
    data_validation_artifact=data_validation.initiate_data_validation()
    logging.info(" data validation completed")
    print(data_validation_artifact)
    
  except Exception as e:
    raise NetworkSecurityException(e,sys)
