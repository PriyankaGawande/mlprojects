'''import sys


def error_massage_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_massage="error occure in python scripts [{0}] line number [{1}] error massage [{2}]" .format(
            file_name,exc_tb.tb_lineno,str(error)
        ) 
    return error_massage

class Custom_Exception(Exception):
        def __init__(self, error_massage,error_detail:sys):
            super().__init__(error_massage)
            self.error_massage=error_massage_details(error_massage,error_detail=error_detail)
        def __str__(self):
            return self.error_massage'''
import sys
from scr.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message