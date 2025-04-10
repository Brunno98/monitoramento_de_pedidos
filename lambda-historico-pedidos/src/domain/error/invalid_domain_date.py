

from domain.error.domain_error import DomainError


class InvalidDomainDateError(DomainError):
    def __init__(self, *args):
        super().__init__(*args)
