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
