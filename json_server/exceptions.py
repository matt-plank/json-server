class HTTPError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code: int = status_code
        self.message: str = message
