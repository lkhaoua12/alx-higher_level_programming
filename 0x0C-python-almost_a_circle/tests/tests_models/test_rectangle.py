import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_rectangle_creation(self):
        rectangle_instance = Rectangle(10, 5)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)



if __name__ == "__main__":
    unittest.main()
