
def area(a: float):
    '''
    находит площадь квадрата

    Параметры: а(float) - длинна стороны квадрата

    Возвращает: float - площадь квадрата
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом")
    return a * a


def perimeter(a: float):
    '''
    находит периметр квадрата

    Параметры: а(float) - длинна стороны квадрата

    Возвращает: float - периметр квадрата
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом")
    return 4 * a
