import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_base_class_creation(self):
        # Test case 1: Check base class creation and ID assignment
        base_instance = Base()
        self.assertIsNotNone(base_instance.id)

    def test_base_class_with_custom_id(self):
        # Test case 2: Check base class creation with custom ID
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_base_class_multiple_instances(self):
        # Test case 3: Check unique ID assignment for multiple instances
        base_instance_1 = Base()
        base_instance_2 = Base()
        base_instance_3 = Base()
        self.assertNotEqual(base_instance_1.id, base_instance_2.id)
        self.assertNotEqual(base_instance_1.id, base_instance_3.id)
        self.assertNotEqual(base_instance_2.id, base_instance_3.id)


if __name__ == "__main__":
    unittest.main()
