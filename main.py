from classes.courier import Courier
from classes.exeptions import BaseError
from classes.request import Request
from classes.shop import Shop
from classes.store import Store


shop = Shop(items={
    'печеньки': 3,
    'собачки': 2,
    'игрушки': 3,
    'шторы': 2
    },
)

store = Store(items={
    'печеньки': 20,
    'собачки': 15,
    'игрушки': 30,
    'шторы': 20,
    'чайники': 30,
    'насосы': 20
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for i in storages:
            print(f'В {i} хранится {storages[i].get_items()}')

        user_input = input('Введите строку формата "доставьте 2 печеньки из склад в магазин". \n'
                           'Введите "стоп" или "stop" чтобы продолжить\n')
        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(user_input, storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request, storages)
        try:
            courier.move()
            print(courier)
        except BaseError as error:
            print(error.message)




if __name__ == '__main__':
    main()
