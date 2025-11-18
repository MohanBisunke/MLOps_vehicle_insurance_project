# from src.logger import logger

# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")


# from src.exception import MyException
# import sys

# try:
#     x = 5 + "10"  # will raise TypeError
# except Exception as e:
#     raise MyException(e)



from src.pipline.training_pipeline import TrainPipeline
pipeline = TrainPipeline()
pipeline.run_pipeline()