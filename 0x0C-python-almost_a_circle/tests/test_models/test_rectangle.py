import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_rectangle_creation(self):
        # Test case 1: Check rectangle creation and attributes
        rectangle_instance = Rectangle(10, 5)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)

    def test_rectangle_area_calculation(self):
        # Test case 2: Check area calculation
        rectangle_instance = Rectangle(10, 5)
        self.assertEqual(rectangle_instance.area(), 50)

    def test_rectangle_update(self):
        # Test case 3: Check update method with *args
        rectangle_instance = Rectangle(10, 5)
        rectangle_instance.update(1, 20)
        self.assertEqual(rectangle_instance.width, 20)
        self.assertEqual(rectangle_instance.height, 5)

        # Test case 4: Check update method with **kwargs
        rectangle_instance.update(y=7, x=2)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 7)

    def test_rectangle_to_dictionary(self):
        # Test case 5: Check to-dictionary conversion
        rectangle_instance = Rectangle(10, 5, 2, 3)
        rect_dict = rectangle_instance.to_dictionary()
        expected_dict = {'id': 7, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(rect_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
