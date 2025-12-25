import unittest
import triangle

class TestTriangle(unittest.TestCase):
    
    def test_area_positive(self):
        """Тест площади треугольника с положительными числами"""
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(10, 0), 0)
        self.assertEqual(triangle.area(7.5, 4.2), 7.5 * 4.2 / 2)
    
    def test_area_negative(self):
        """Тест площади треугольника с отрицательными числами"""
        self.assertEqual(triangle.area(-10, 5), -25)
        self.assertEqual(triangle.area(10, -5), -25)
    
    def test_perimeter_positive(self):
        """Тест периметра треугольника с положительными числами"""
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(5.5, 6.5, 7.5), 19.5)
    
    def test_perimeter_negative(self):
        """Тест периметра треугольника с отрицательными числами"""
        self.assertEqual(triangle.perimeter(-3, -4, -5), -12)

    def test_invalid_input(self):
        """Тест с некорректными входными данными"""
        with self.assertRaises(TypeError):
            triangle.area("строка", 5)
        with self.assertRaises(TypeError):
            triangle.area(5, "строка")
        with self.assertRaises(TypeError):
            triangle.perimeter("a", "b", "c")

if __name__ == '__main__':
    unittest.main()