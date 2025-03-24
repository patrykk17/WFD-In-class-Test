import unittest
from PartA import Pet, Dog

class TestPetAndDog(unittest.TestCase):

    def setUp(self):
        # Create test objects
        self.pet = Pet("Milo", 3, "Male", "P001", "Alice")
        self.dog = Dog("Buddy", 5, "Male", "D001", "Bob", "Labrador", True)
        self.same_dog = self.dog  # used for identity test
        self.different_dog = Dog("Buddy", 5, "Male", "D001", "Bob", "Labrador", True)

    # Test if object is instance of a class
    def test_instance_of_pet(self):
        self.assertIsInstance(self.pet, Pet)
        self.assertIsInstance(self.dog, Dog)
        self.assertIsInstance(self.dog, Pet)  # because Dog inherits from Pet

    # Test if object is NOT instance of a class
    def test_not_instance(self):
        self.assertNotIsInstance(self.pet, Dog)
        self.assertNotIsInstance("not a pet", Pet)

    # Test if 2 objects are identical (same object in memory)
    def test_objects_identity(self):
        self.assertIs(self.dog, self.same_dog)
        self.assertIsNot(self.dog, self.different_dog)

    #   Test update methods
    def test_update_pet_attributes(self):
        self.pet.update_name("Milo Jr.")
        self.assertEqual(self.pet.name, "Milo Jr.")

        self.pet.update_age(4)
        self.assertEqual(self.pet.age, 4)

        self.pet.update_sex("Female")
        self.assertEqual(self.pet.sex, "Female")

        self.pet.update_petID("P002")
        self.assertEqual(self.pet.petID, "P002")

        self.pet.update_owner_name("Eve")
        self.assertEqual(self.pet.owner_name, "Eve")

    def test_update_dog_attributes(self):
        self.dog.update_breed("Golden Retriever")
        self.assertEqual(self.dog.breed, "Golden Retriever")

        self.dog.update_is_trained(False)
        self.assertFalse(self.dog.is_trained)



if __name__ == '__main__':
    unittest.main()
