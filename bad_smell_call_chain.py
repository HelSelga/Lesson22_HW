# Измените класс Person так, чтобы его методы оперировали внутренним состоянием,
# а не использовали цепочку вызовов объектов

# Исходный код
# class Room:
#     def get_name(self):
#         return 42
#
#
# class Street:
#     def get_room(self) -> Room:
#         return Room()
#
#
# class City:
#     def get_street(self) -> Street:
#         return Street()
#
#     def population(self):
#         return 100500
#
#
# class Country:
#     def get_city(self) -> City:
#         return City()
#
#
# class Planet:
#     def get_country(self) -> Country:
#         return Country()
#
#
# class Person:
#     def __init__(self):
#         self.planet = Planet()
#
#     def get_person_room(self):
#         return self.planet.get_country().get_city().get_street().get_room().get_name()
#
#     def get_city_population(self):
#         return self.planet.get_country().get_city().population()

# Решение
class Person:
    def __init__(self, city_population, room_number):
        self.city_population = city_population
        self.room_number = room_number

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.city_population
