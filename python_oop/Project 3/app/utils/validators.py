# validators module

import numbers


def validate_integer(
        arg_name, arg_value, min_value=None, max_value=None
):
    if not isinstance(arg_value, numbers.Integral):
        raise TypeError(f'{arg_name} must be integer')

    if min_value is not None and arg_value < min_value:
        raise ValueError(f'{arg_name} must be greater min_value={min_value}')

    if max_value is not None and arg_value > max_value:
        raise ValueError(f'{arg_name} must be less max_value={max_value}')


def validate_str(
        arg_name, arg_value
):
    if not isinstance(arg_value, str):
        raise TypeError(f'{arg_name} must be string')

    if len(arg_value.split()) == 0:
        raise ValueError(f'{arg_name} cannot be empty')

    if arg_value[0].isdigit():
        raise ValueError(f'{arg_name} cannot start with a number')
