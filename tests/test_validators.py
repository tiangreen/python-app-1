import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.validators import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "test@example.com",
        "user.name+tag+sorting@example.co.uk",
        "user_name@example.io",
    ],
)
def test_valid_emails(email):
    assert is_valid_email(email)


@pytest.mark.parametrize(
    "email",
    [
        "invalidemail",
        "user@",
        "user@.com",
    ],
)
def test_invalid_emails(email):
    assert not is_valid_email(email)
