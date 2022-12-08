

class Flight:
    def __init__(self, city_from, city_to):
        self.__sity_from = city_from
        self.__city_to = city_to

    def __str__(self):
        return f"{self.__class__.__name__} from {self.__sity_from} to {self.__city_to}"

route = Flight(input(), input())
print(route)
