import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    def test_square_creation(self):
        # Test case 1: Check square creation and attributes
        square_instance = Square(5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)

    def test_square_area_calculation(self):
        # Test case 2: Check area calculation
        square_instance = Square(5)
        self.assertEqual(square_instance.area(), 25)

    def test_square_update(self):
        # Test case 3: Check update method with *args
        square_instance = Square(5)
        square_instance.update(1, 10)
        self.assertEqual(square_instance.width, 10)
        self.assertEqual(square_instance.height, 10)

        # Test case 4: Check update method with **kwargs
        square_instance.update(y=7, x=2)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 7)

    def test_square_to_dictionary(self):
        # Test case 5: Check to-dictionary conversion
        square_instance = Square(5, 2, 3)
        square_dict = square_instance.to_dictionary()
        expected_dict = {'id': 8, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
