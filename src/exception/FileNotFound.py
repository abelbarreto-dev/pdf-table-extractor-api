from src.exception.HttpBaseException import HttpBaseException


class FileNotFound(HttpBaseException):
    def __init__(self, message: str = "file not found") -> None:
        super().__init__("file not found", 404)
