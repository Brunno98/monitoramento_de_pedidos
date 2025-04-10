
from domain.error.invalid_domain_date import InvalidDomainDateError
from datetime import datetime, timezone

VALID_FORMATS = [
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S",
]


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
    def from_str(cls, input: str) -> 'DomainDate':
        for format in VALID_FORMATS:
            try:
                return cls(datetime.strptime(input, format))
            except ValueError:
                continue
        raise InvalidDomainDateError(
            f"Formato de data inválido: '{input}'. Formatos aceitos: {VALID_FORMATS}"
        )

    @property
    def value(self) -> datetime:
        return self.__value.replace(tzinfo=None)

    def __str__(self):
        return self.__value.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __eq__(self, other):
        if not isinstance(other, DomainDate):
            return NotImplemented
        return self.value == other.value
