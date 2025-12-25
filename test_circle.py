import unittest
import math
import circle

class TestCircle(unittest.TestCase):
    
    def test_area_positive(self):
        """Тест площади круга с положительными числами"""
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
        self.assertAlmostEqual(circle.area(0), 0)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)
    
    def test_area_negative(self):
        """Тест площади круга с отрицательными числами"""
        self.assertAlmostEqual(circle.area(-5), math.pi * 25)
    
    def test_perimeter_positive(self):
        """Тест длины окружности с положительными числами"""
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(circle.perimeter(0), 0)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)
    
    def test_perimeter_negative(self):
        """Тест длины окружности с отрицательными числами"""
        self.assertAlmostEqual(circle.perimeter(-5), 2 * math.pi * -5)
    
    def test_edge_cases(self):
        """Тест граничных случаев"""
        # Очень маленький радиус
        self.assertAlmostEqual(circle.area(0.0001), math.pi * 0.00000001)
        # Очень большой радиус
        self.assertAlmostEqual(circle.area(1000), math.pi * 1000000)
        
    def test_invalid_input(self):
        """Тест с некорректными входными данными"""
        with self.assertRaises(TypeError):
            circle.area("строка")
        with self.assertRaises(TypeError):
            circle.perimeter("строка")

if __name__ == '__main__':
    unittest.main()