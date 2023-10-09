import logging
import re
import pytest
import itertools

logger = logging.getLogger(__name__)


def check_num_is_odd(num: int):
    if num is not int:
        return Exception
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False


@pytest.mark.parametrize(
    "num, expected",  # parameters names
    [
        (1, False),
        (2, True),
        (0, True),
        (-2, True),
        (-1, False),
    ]   # list of tests values: each value is 2-tuple because we have 2 params
)
def test_check_num__logic(
    num,
    expected
):
    result = check_num_is_odd(num)
    logger.debug(f"Result: {result}")
    assert result is expected


@pytest.mark.parametrize(
    "num, expected",
    [
        ('word', Exception),
        (list, Exception),
        (1.3, Exception),
    ]
)
def test_check_num__exc(
    num,
    expected
):

    result = check_num_is_odd(num)

    logger.debug(f"Result: {result}")
    assert result is expected


def check_valid_name(name: str):
    reg_pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
    pattern = re.compile(reg_pattern)
    match = re.match(pattern, name)
    if match:
        return True
    else:
        return False


@pytest.mark.parametrize(
    "name, expected",
    [
        ('Mark Godard', True),
        ('Ji Pin', True),
        ('Pavel', False),
        ('ivan Potan', False),
        ('Victor tsoi', False),
        ('Витя Фомин', False),
        ('AbramLincoln', False),
        ('Xc9Ra9', False),
        ('12345', False),
        ('Adam12 Sandler', False),
    ]
)
def test_check_valid_name(
    name,
    expected
):

    result = check_valid_name(name)

    logger.debug(f"Result: {result}")

    assert result is expected
