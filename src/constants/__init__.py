import os 
from datetime import time


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

##data ingestion
DATA_INGESTION_COLLECTION_NAME : str ="Dataset1"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str= "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO :float = 0.25

