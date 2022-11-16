from classes.abstract_storage import AbstractStorage
from classes.request import Request
from classes.store import Store
from classes.shop import Shop


class Courier:
    def __init__(self, request: Request, storages: dict[str, AbstractStorage]):
        self.__request = request
        self.__from = storages[self.__request.departure]
        self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        self.__to.add(name=self.__request.product, amount=self.__request.amount)

    def __repr__(self):
        return f'Нужное количество есть на складе\n' \
               f'Курьер забрал {self.__request.amount} {self.__request.product} со {self.__request.departure}\n' \
               f'Курьер везет {self.__request.amount} {self.__request.product} со {self.__request.departure} в {self.__request.destination}\n' \
               f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}'