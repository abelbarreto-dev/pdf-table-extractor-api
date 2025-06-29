class HttpBaseException(Exception):
    code: int

    def __init__(self, message: str, code: int):
        self.code = code
        super().__init__(message)
