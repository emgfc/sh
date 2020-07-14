from typing import Dict, Any


class ApiError(Exception):
    status_code = 500

    def __init__(self, message: str, status_code: int = None) -> None:
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self.status_code,
            'message': self.message
        }


class InvalidUsage(ApiError):
    status_code = 400

    def __init__(self, message: str, status_code: int = None) -> None:
        ApiError.__init__(self, message, status_code)


class NoResourceFound(ApiError):
    status_code = 404

    def __init__(self, message: str, status_code: int = None) -> None:
        ApiError.__init__(self, message, status_code)


class NotAllowed(ApiError):
    status_code = 405

    def __init__(self, message: str, status_code: int = None) -> None:
        ApiError.__init__(self, message, status_code)
