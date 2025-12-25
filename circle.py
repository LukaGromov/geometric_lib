import math


def area(r : float):
    '''
    находит площадь круга

    Параметры: r (float) - радиус круга

    Возвращает: float - площадь круга
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус круга должен быть числом")
    return math.pi * r * r


def perimeter(r : float):
    '''
    находит длинну окружности

    Параметры: r (float) - радиус окружности

    Возвращает: float - длинна окружности
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус круга должен быть числом")
    return 2 * math.pi * r
