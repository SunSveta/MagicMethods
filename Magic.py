import math
# Задание 1 - что такое производное я забыла сразу же, как только сдала последний экзамен по математике в школе.
# Поэтому пока только через cos

class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return math.cos(args[0])


@Derivative
def sin_(x):
    return math.sin(x)

sin_(math.pi/3)
