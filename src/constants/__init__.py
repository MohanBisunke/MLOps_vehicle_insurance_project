import os 
from datetime import date


#MONGODB BASED CONSTANT
DATABASE_NAME= "Mohan1"
COLLECTION_NAME="Dataset1"
MONGODB_URL_KEY= "MONGODB_URL"

FILE_NAME :str = "data.csv"
TRAIN_FILE_NAME :str = "train.csv"
TEST_FILE_NAME : str = "test.csv"


#pipeline
PIPELINE_NAME : str =""
ARTIFACT_DIR :str = "artifact"


TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year


#schema file path
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

##data ingestion
DATA_INGESTION_COLLECTION_NAME : str ="Dataset1"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str= "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO :float = 0.25


##data validation
DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME :str = "reports.yaml"


## data_transformation
DATA_TRANSFORMATION_DIR_NAME : str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR :str ="transformed_object"
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"

