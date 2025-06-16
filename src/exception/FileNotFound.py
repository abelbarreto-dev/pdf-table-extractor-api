from src.exception.HttpBaseException import HttpBaseException


class FileNotFound(HttpBaseException):
    def __init__(self, message: str = "file not found", code: int = 404) -> None:
        super().__init__(message, code)
