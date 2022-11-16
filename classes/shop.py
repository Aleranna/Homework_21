from classes.base_storage import BaseStorage
from classes.exeptions import TooManyDifferentObjectsError


class Shop(BaseStorage):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_item_count() >= 5:
            raise TooManyDifferentObjectsError
        super().add(name, amount)
