import sys
from src.logger import logger  # use the configured logger

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.
    """
    # Get exception info from the current exception
    exc_type, exc_obj, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    # Formatted error message
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log using the custom logger
    logger.error(error_message)
    
    return error_message


class MyException(Exception):
    """
    Custom exception class for detailed error reporting.
    """
    def __init__(self, error: Exception):
        """
        Initializes the exception with detailed information.

        :param error: The original exception object.
        """
        # Format the detailed error message
        self.error_message = error_message_detail(error, sys)
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message
