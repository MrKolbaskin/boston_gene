# test for validators.py

import pytest

from app.utils.validators import validate_integer, validate_str


class TestIntegerValidator:
    def test_valid(self):
        validate_integer('arg', 10, min_value=0, max_value=100)

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer('arg', 2.5)

        with pytest.raises(ValueError):
            validate_integer('arg', 10, 2, 5)


class TestStringValidator():
    def test_valid(self):
        validate_str('arg', 'Hello')
