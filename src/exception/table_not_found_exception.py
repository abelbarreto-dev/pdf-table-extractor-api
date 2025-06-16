from src.exception.http_base_exception import HttpBaseException


class TableNotFoundException(HttpBaseException):
    def __init__(self, message: str = "not tables found at file", code: int = 400):
        super().__init__(message, code)
