import doctest
from typing import Union


class Arthropod:
    """
    Создание и подготовка к работе объекта "Членистоногое".

    :param name: Название членистоногого
    :param paws: Количество ног у членистоногого
    :param eyes: Количество сегментов тела

    Примеры:
    >>> scorpion_arthropod = Arthropod("Scorpion", 6, 4)
    """

    def __init__(self, name: str, paws: int, eyes: int):
        self.name = name
        self.paws = paws
        self.eyes = eyes
        self._wings = False  # Инкапсулированный атрибут

    def has_wings(self) -> bool:
        """
        Проверяет, есть ли у членистоногого крылья.
        :return: True, если есть, False, если нет

        Примеры:
        >>> scorpion_arthropod = Arthropod("Scorpion", 6, 4)
        >>> scorpion_arthropod.has_wings()
        False
        """
        return self._wings

    def enable_wings(self) -> None:
        """
        Включает наличие крыльев у членистоногого.

        Примеры:
        >>> scorpion_arthropod = Arthropod("Scorpion", 6, 4)
        >>> scorpion_arthropod.enable_wings()
        >>> scorpion_arthropod.has_wings()
        True
        """
        self._wings = True

    def move(self) -> str:
        """
        Возвращает строку с описанием движения.
        :return: Описание движения.

         Примеры:
        >>> scorpion_arthropod = Arthropod("Scorpion", 6, 4)
        >>> scorpion_arthropod.move()
        'Scorpion moves using its 6 paws.'
        """
        return f"{self.name} moves using its {self.paws} paws."

    def __str__(self) -> str:
        wing_status = "with wings" if self._wings else "without wings"
        return (
            f"Arthropod: {self.name}, {self.paws} paws, {self.eyes} eyes, {wing_status}"
        )

    def __repr__(self) -> str:
        return f"Arthropod(name='{self.name}', paws={self.paws!r}, eyes={self.eyes!r}, wings={self._wings!r})"


class Insect(Arthropod):
    """
    Создание и подготовка к работе объекта "Насекомое".

    :param name: Название насекомого
    :param eyes: Количество глаз тела
    :param antennas: Количество усиков
    :param wings: Наличие крыльев (по умолчанию False)

    Примеры:
    >>> flea = Insect("Flea", 2, 2)
    """

    def __init__(self, name: str, eyes: int, antennas: int, wings: bool = False):
        super().__init__(name, paws=6, eyes=eyes)
        self.antennas = antennas
        if wings:
            self.enable_wings()
            
    def __str__(self) -> str:
        wing_status = "with wings" if self._wings else "without wings"
        return f"Insect: {self.name}, {self.paws} paws, {self.eyes} eyes, {self.antennas} antennas, {wing_status}"

    def __repr__(self) -> str:
        return f"Insect(name='{self.name}', paws={self.paws!r}, eyes={self.eyes!r}, antennas={self.antennas!r}, wings={self._wings!r})"

    def move(self) -> str:
        """
        Возвращает строку с описанием движения насекомого.
        Переопределенный метод, т.к. у насекомых есть возможность летать.
        :return: Описание движения насекомого

        Примеры:
        >>> flea = Insect("Flea", 2, 2)
        >>> flea.move()
        'Flea crawls using its 6 paws.'
        >>> butterfly = Insect("Butterfly", 3, 2, True)
        >>> butterfly.move()
        'Butterfly flies using its wings and moves using its 6 paws.'
        """
        if self._wings:
            return f"{self.name} flies using its wings and moves using its {self.paws} paws."
        return f"{self.name} crawls using its {self.paws} paws."


if __name__ == "__main__":
    doctest.testmod()
