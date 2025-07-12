import re

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    """Return True if the provided email address is valid.

    The validation uses a regular expression and requires at least one
    character before and after the ``@`` and a valid top level domain.
    """
    return bool(EMAIL_REGEX.fullmatch(email))
