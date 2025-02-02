import doctest
from typing import Union


class Smartphone:
    def __init__(self, memory: int, battery: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param memory: Объем памяти в смартфоне, в Гб
        :param battery: Объем батареи смартфона, в мАч

        Примеры:
        >>> iPhone = Smartphone(128, 2000)  # инициализация экземпляра класса
        """
        if not isinstance(memory, int):
            raise TypeError("Объем памяти должно быть целым числом")
        if memory < 0:
            raise ValueError("Объем памяти не может быть отрицательно")
        self.memory = memory

        if not isinstance(battery, (int, float)):
            raise TypeError("Объем батареи должен быть числом")
        if battery < 0:
            raise ValueError("Объем батареи не может быть отрицательным")
        self.battery = battery

    def smartphone_increase_memory(self, sd_memory: int) -> None:
        """
               Увеличение памяти.
               :param sd_memory: Добавление памяти через использование sd карты

               :raise ValueError: Вызываем ошибку, если отсутствует слот под sd-карту

               Примеры:
               >>> iPhone = Smartphone(128, 2000)
               >>> iPhone.smartphone_increase_memory(32)
               """
        if not isinstance(sd_memory, int):
            raise TypeError("Объем sd-карты должен быть целым числом")
        if sd_memory < 0:
            raise ValueError("Объем sd-карты не должен быть отрицательным")
        ...

    def is_smartphone_nfc(self) -> bool:
        """
               Функция проверки наличия NFC в смартфоне.
               :return: Есть ли NFC в смартфоне

               Примеры:
               >>> iPhone = Smartphone(128, 2000)
               >>> iPhone.is_smartphone_nfc()
               """
        ...


class Car:
    def __init__(self, weightlifters_weight: Union[int, float], weightlifter_height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Машина"

        :param weightlifters_weight: Вес штангиста
        :param weightlifter_height: Рост штангиста

        Примеры:
        >>> Schwarzenegger = Car(110, 185)# инициализация экземпляра класса
        """
        if not isinstance(weightlifters_weight, (int, float)):
            raise TypeError("Вес штангиста должен быть числом")
        if weightlifters_weight < 0:
            raise ValueError("Вес штангиста должен быть положительным числом")
        self.weightlifters_weight = weightlifters_weight

        if not isinstance(weightlifter_height, (int, float)):
            raise TypeError("Рост штангиста должен быть числом")
        if weightlifter_height < 0:
            raise ValueError("Рост штангиста  не может быть отрицательным числом")
        self.weightlifter_height = weightlifter_height

    def car_wins(self, number_wins: Union[int, float]) -> None:
        """
               Перезарядка оружия.
               :param number_wins: Количество завоеванных побед

               :raise ValueError: Вызываем ошибку, если количество побед не является числом

               Примеры:
               >>> Schwarzenegger = Car(110, 185)
               >>> Schwarzenegger.car_wins(7)
               """
        if not isinstance(number_wins, (int, float)):
            raise TypeError("Количество побед должно быть числом")
        if number_wins < 0:
            raise ValueError("Количество побед не может быть отрицательно")
        ...

    def weight_bench(self, number_kg: Union[int, float]) -> None:
        """
               Перезарядка оружия.
               :param number_kg: Вес штанги на жиме лежа

               :raise ValueError: Вызываем ошибку, если Вес штанги не является числом

               Примеры:
               >>> Schwarzenegger = Car(110, 185)
               >>> Schwarzenegger.weight_bench(227)
               """
        if not isinstance(number_kg, (int, float)):
            raise TypeError("Вес штанги должен быть числом")
        if number_kg < 0:
            raise ValueError("Вес штанги не может быть отрицательно")
        ...

    def is_car_use_doping(self) -> bool:
        """
               Функция которая проверяет использовал ли штангист допинг.
               :return: использует ли штангист допинг

               Примеры:
               >>> Schwarzenegger = Car(110, 185)
               >>> Schwarzenegger.is_car_use_doping()
               """
        ...


class Arthropods:
    def __init__(self, paws: int, eyes: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Членистоногие"

        :param paws: Количество лап у насекомого
        :param eyes: Количество глаз у насекомого

        Примеры:
        >>> spider = Arthropods(8, 6)  # инициализация экземпляра класса
        """
        if not isinstance(paws, int):
            raise TypeError("Количество лап должно быть целым числом")
        if paws <= 0:
            raise ValueError("Количество лап должно быть положительным числом")
        self.paws = paws

        if not isinstance(eyes, (int, float)):
            raise TypeError("Количество глаз должно быть числом")
        if eyes < 0:
            raise ValueError("Количество глаз не может быть отрицательным числом")
        self.eyes = eyes

    def arthropods_danger(self) -> bool:
        """
               Функция проверки наличия яда у членистоногого.
               :return: Есть ли яд у членистоного

               Примеры:
               >>> spider = Arthropods(8, 6)
               >>> spider.arthropods_danger()
               """

    def arthropods_claws(self) -> bool:
        """
               Функция проверки наличия клешней у членистоногого.
               :return: Есть ли клешни у членистоного

               Примеры:
               >>> spider = Arthropods(8, 6)
               >>> spider.arthropods_claws()
               """

if __name__ == "__main__":
    doctest.testmod()  # Проводим проверку примеров, приведенных в документации
