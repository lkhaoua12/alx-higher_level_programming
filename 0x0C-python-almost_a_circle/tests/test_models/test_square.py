import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareClass(unittest.TestCase):
    def test_square_creation(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.width, 5)
        self.assertEqual(square_instance.height, 5)


if __name__ == "__main__":
    unittest.main()
