import os 
import certifi
import sys
import pymongo

from src.exception import MyException
from src.logger import logger
from src.constants import DATABASE_NAME, MONGODB_URL_KEY


# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()


class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB database.

    Attributes:
    ----------
    client : MongoClient
        A shared MongoClient instance for the class.
    database : Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    -------
    __init__(database_name: str) -> None
        Initializes the MongoDB connection using the given database name.
    """
    
    client = None
    
    
    def __init__(self, database_name: str = DATABASE_NAME) ->None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        ------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """
        
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if mongodb_url is None:
                        raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                    
                MongoDBClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
                
                self.client = MongoDBClient.client
                self.database = self.client[database_name]  # Connect to the specified database
                self.database_name = database_name
                logger.info("MongoDB connection successful.")
                
        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)