import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_base_class_creation(self):
        base_instance = Base()
        self.assertIsNotNone(base_instance.id)

    def test_base_class_with_custom_id(self):
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)



if __name__ == "__main__":
    unittest.main()
