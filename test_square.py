import unittest
import square

class TestSquare(unittest.TestCase):
    
    def test_area_positive(self):
        """Тест площади квадрата с положительными числами"""
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(2.5), 6.25)
        self.assertEqual(square.area(0), 0)
    
    def test_area_negative(self):
        """Тест площади квадрата с отрицательными числами"""
        self.assertEqual(square.area(-5), 25)  # Квадрат отрицательного числа
        
    def test_perimeter_positive(self):
        """Тест периметра квадрата с положительными числами"""
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(2.5), 10)
        self.assertEqual(square.perimeter(0), 0)
    
    def test_perimeter_negative(self):
        """Тест периметра квадрата с отрицательными числами"""
        self.assertEqual(square.perimeter(-5), -20)
    
    def test_invalid_input(self):
        """Тест с некорректными входными данными"""
        with self.assertRaises(TypeError):
            square.area("строка")
        with self.assertRaises(TypeError):
            square.perimeter("строка")

if __name__ == '__main__':
    unittest.main()