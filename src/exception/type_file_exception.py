from src.exception.http_base_exception import HttpBaseException


class TypeFileException(HttpBaseException):
    def __init__(self, message: str = "file type not expected", code: int = 400) -> None:
        super().__init__(message, code)
