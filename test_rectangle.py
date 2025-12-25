import unittest
import rectangle

class TestRectangle(unittest.TestCase):
    
    def test_area_positive(self):
        """Тест площади прямоугольника с положительными числами"""
        self.assertEqual(rectangle.area(10, 5), 50)
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(7.5, 4.2), 31.5)
    
    def test_area_negative(self):
        """Тест площади прямоугольника с отрицательными числами"""
        self.assertEqual(rectangle.area(-10, 5), -50)
        self.assertEqual(rectangle.area(10, -5), -50)
    
    def test_perimeter_positive(self):
        """Тест периметра прямоугольника с положительными числами"""
        self.assertEqual(rectangle.perimeter(10, 5), 30)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        self.assertEqual(rectangle.perimeter(7.5, 4.2), 2 * (7.5 + 4.2))
    
    def test_perimeter_negative(self):
        """Тест периметра прямоугольника с отрицательными числами"""
        self.assertEqual(rectangle.perimeter(-10, -5), -30)
    
    def test_square_case(self):
        """Тест частного случая - квадрат"""
        side = 5
        self.assertEqual(rectangle.area(side, side), 25)
        self.assertEqual(rectangle.perimeter(side, side), 20)

if __name__ == '__main__':
    unittest.main()