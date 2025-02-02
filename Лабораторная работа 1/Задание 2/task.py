from task_1 import Smartphone, Car, Arthropods

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        smartphone1 = Smartphone(256, 3000)
        smartphone1.smartphone_increase_memory(-32)
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        car1 = Car("may", 210)
    except TypeError:
        print("Ошибка: неправильные данные")

    try:
        arthropods1 = Arthropods(24, "-5")
    except TypeError:
        print("Ошибка: неправильные данные")
