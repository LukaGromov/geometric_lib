import math


def area(r):
    '''
    находит площадь круга

    Параметры: r (float) - радиус круга

    Возвращает: float - площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    находит длинну окружности

    Параметры: r (float) - радиус окружности

    Возвращает: float - длинна окружности
    '''
    return 2 * math.pi * r
