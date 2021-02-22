class Timeout(Exception):
    """Timeout"""


class MissingParameters(Exception):
    """Missing Parameters"""


class PermissionsDenied(Exception):
    """Permissions Denied"""


class InvalidToken(Exception):
    """Invalid Token"""


class InvalidPassword(Exception):
    """Invalid Password"""


class UsernameAlreadyExists(Exception):
    """Username already exists"""


class MicroServiceExpeption(Exception):
    def __init__(self, error):
        self.msg = error


class InvalidServerResponse(Exception):
    """Invalid Server Response"""


class InvalidInputData(Exception):
    """Invalid Input Date MS Error"""
