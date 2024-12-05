# Домашняя работа по уроку "Специальные методы классов"

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли указанное количество этажей
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Вывод этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращает количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращает строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Пример использования метода __str__
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 20

# Пример использования метода __len__
print(len(h1))  # Ожидаемый вывод: 10
print(len(h2))  # Ожидаемый вывод: 20

