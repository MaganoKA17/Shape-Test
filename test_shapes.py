import unittest
from shapes import Square, Circle, Rectangle
import math

class TestShapes(unittest.TestCase):

    #Test polymorphism: name method override
    def test_square_name(self):
        s = Square()
        self.assertEqual(s.name(), "Square")

    #Test Circle area
    def test_circle_area(self):
        c = Circle(5)
        expected = math.pi * 5 * 5
        self.assertAlmostEqual(c.area(), expected)

    #Test Rectangle area
    def test_rectangle_area(self):
        r = Rectangle(4, 3)
        self.assertEqual(r.area(), 12)

    #Test attributes are stored correctly
    def test_circle_radius_attribute(self):
        c = Circle(7)
        self.assertEqual(c.radius, 7)

    def test_rectangle_dimensions(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)


if __name__ == "__main__":
    unittest.main()