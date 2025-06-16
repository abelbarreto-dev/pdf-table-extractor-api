from src.exception.http_base_exception import HttpBaseException


class FileNotFoundException(HttpBaseException):
    def __init__(self, message: str = "file not found", code: int = 404) -> None:
        super().__init__(message, code)
