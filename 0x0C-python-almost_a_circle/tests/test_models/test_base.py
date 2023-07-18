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

    def test_base_to_json_string(self):
        # Test case 4: Check to_json_string method
        base_instance = Base(5)
        base_dict = base_instance.to_dictionary()
        base_json_string = Base.to_json_string([base_dict])
        expected_json_string = '[{"id": 5}]'
        self.assertEqual(base_json_string, expected_json_string)

    def test_base_from_json_string(self):
        # Test case 5: Check from_json_string method
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        base_list = Base.from_json_string(json_string)
        self.assertEqual(len(base_list), 3)
        self.assertEqual(base_list[0].id, 1)
        self.assertEqual(base_list[1].id, 2)
        self.assertEqual(base_list[2].id, 3)


if __name__ == "__main__":
    unittest.main()
