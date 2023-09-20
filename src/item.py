from csv import DictReader
from pathlib import Path
from settings import CURRENT_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    FILE_CSV = Path.joinpath(CURRENT_PATH, "src", "items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        new_price = self.price * Item.pay_rate
        return new_price

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        filename = cls.FILE_CSV
        with open(filename, encoding="windows-1251", newline='') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                name = row["name"]
                price = row["price"]
                quantity = row["quantity"]
                cls(str(name), float(price), int(quantity))

    @staticmethod
    def string_to_number(number):
        number_new = int(float(number))
        return number_new



