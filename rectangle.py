def area(a : float, b : float):
   '''
    находит площадь прямоугльника

    Параметры: а(float) - ширина прямоугольника, b (float) - высота прямоугольника

    Возвращает: float - площадь прямоугольника
    '''
   if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ширина и высота прямоугольника должны быть числами")
   return a * b
 
def perimeter(a : float, b : float):
   '''
    находит периметр прямоугльника

    Параметры: а(float) - ширина прямоугольника, b (float) - высота прямоугольника

    Возвращает: float - периметр прямоугольника
    '''
   if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ширина и высота прямоугольника должны быть числами")
   return 2 * (a + b)
