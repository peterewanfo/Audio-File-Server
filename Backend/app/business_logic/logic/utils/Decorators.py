import jwt, time
from functools import wraps
from config import config
from flask import request, make_response
from app.business_logic.logic.utils.DBFunctionsClass import DBFunctionsClass

def manage_db_connection(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):

        function_return_data = func(*args, **kwargs)

        #MANAGE DATABASE CONNECTION
        DBFunctionsClass.manageDBConnection()

        return function_return_data

    return wrapper_function
