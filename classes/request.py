from classes.abstract_storage import AbstractStorage
from classes.exeptions import InvalidRequestError, UnknownStorageError


class Request:
    def __init__(self, request_str, storages: dict[str, AbstractStorage]):
        request = request_str.lower().split(' ')
        if len(request) != 7:
            raise InvalidRequestError

        self.amount = int(request[1])
        self.product = request[2]
        self.destination = request[6]
        self.departure = request[4]

        if self.destination not in storages or self.departure not in storages:
            raise UnknownStorageError



