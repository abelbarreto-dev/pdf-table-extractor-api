import functools
import json

from flask import Response

from src.exception.http_base_exception import HttpBaseException


def exception_handler(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except HttpBaseException as ex:
            response = Response(
                status=ex.code,
                mimetype="application/json"
            )
            response.data = json.dumps({"error": ex.args[0]})
            return response

    return wrapper
