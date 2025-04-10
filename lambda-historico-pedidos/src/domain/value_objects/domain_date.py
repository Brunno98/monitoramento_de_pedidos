
from domain.error.invalid_domain_date import InvalidDomainDateError
from datetime import datetime, timezone


class DomainDate:

    def __init__(self, date: datetime):
        if not date:
            raise InvalidDomainDateError("Data não pode ser nula")
        if not isinstance(date, datetime):
            raise InvalidDomainDateError(
                f"Valor {date} precisa ser do tipo 'datetime'")
        self.__value = date

    @classmethod
    def now(cls) -> 'DomainDate':
        return cls(datetime.now())

    @classmethod
    def from_timestamp(cls, timestamp: float, tz=timezone.utc) -> 'DomainDate':
        return cls(datetime.fromtimestamp(timestamp, tz))

    @classmethod
    def from_str(cls, input: str, format="%Y-%m-%dT%H:%M:%S.%f") -> 'DomainDate':
        return cls(datetime.strptime(input, format))

    @property
    def value(self) -> datetime:
        return self.__value

    def __str__(self):
        return self.__value.strftime("%Y-%m-%dT%H:%M:%S.%f")
