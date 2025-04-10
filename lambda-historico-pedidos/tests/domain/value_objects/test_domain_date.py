from datetime import datetime
from freezegun import freeze_time
import pytest
from domain.value_objects.domain_date import DomainDate
from domain.error.domain_error import DomainError


def test_given_a_date_as_string__when_create_a_domain_date__should_create_it():
    # given
    expected_date = "2025-04-10T12:01:02.123456"

    # when
    domain_date = DomainDate.from_str(expected_date)

    # then
    assert domain_date
    assert str(domain_date) == expected_date


def test_given_a_timestamp__when_create_a_domain_date__should_create_it():
    # given
    timestamp = 1744305816  # Thursday, 10 April 2025 17:23:36
    expected_date = "2025-04-10T17:23:36.000000"

    # when
    domain_date = DomainDate.from_timestamp(timestamp)

    # then
    assert domain_date
    assert str(domain_date) == expected_date


@freeze_time("2025-04-10T17:23:36.123456")
def test__when_create_a_now_domain_date__should_create_it():
    # when
    domain_date = DomainDate.now()

    # then
    assert domain_date
    assert str(domain_date) == "2025-04-10T17:23:36.123456"


def test_given_a_invalid_value__when_create_a_domain_date__should_raise_domain_error():
    try:
        DomainDate("invalid")
    except DomainError:
        assert True
    else:
        assert False


def test_given_an_Empty_value__when_create_a_domain_date__should_raise_domain_error():
    try:
        DomainDate(None)
    except DomainError:
        assert True
    else:
        assert False


@pytest.mark.parametrize("input_str,expected", [
    ("2025-04-10T13:45:00", datetime(2025, 4, 10, 13, 45, 0)),
    ("2025-04-10T13:45:00.123456", datetime(2025, 4, 10, 13, 45, 0, 123456)),
    ("2025-04-10T13:45:00.000000", datetime(2025, 4, 10, 13, 45, 0, 0)),
    ("2025-04-10 13:45:00", datetime(2025, 4, 10, 13, 45, 0)),
    ("2025-04-10 13:45:00.123456", datetime(2025, 4, 10, 13, 45, 0, 123456)),
    ("2025-04-10 13:45:00.000000", datetime(2025, 4, 10, 13, 45, 0, 0)),
])
def test_domain_date_from_str(input_str, expected):
    domain_date = DomainDate.from_str(input_str)
    assert domain_date.value == expected
