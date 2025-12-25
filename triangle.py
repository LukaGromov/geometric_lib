def area(a : float, h : float):
   '''
    находит площадь треугольника

    Параметры: а(float) - сторона треугольника, h(float) - высота, опущенная на нее

    Возвращает: float - площадь треугольника
    '''
   if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Сторона и высота треугольника должны быть числами")
   return a * h / 2
 
def perimeter(a : float, b : float, c : float):
    '''
    находит периметр треугольника

    Параметры: а, b, c(float) - длинны сторон треугольника

    Возвращает: float - периметр квадрата
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все стороны треугольника должны быть числами")
    return a + b + c
