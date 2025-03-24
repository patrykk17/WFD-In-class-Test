class Pet:
    def __init__(self, name: str, age: int, sex: str, petID: str, owner_name: str):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name

    # Method to print all attributes of the Pet
    def print_attributes(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Pet ID: {self.petID}")
        print(f"Owner Name: {self.owner_name}")

    # Method to update the name of the pet
    def update_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Invalid type for name.")

    # Method to update the age of the pet
    def update_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            print("Invalid type for age.")

    # Method to update the sex of the pet
    def update_sex(self, sex):
        if isinstance(sex, str):
            self.sex = sex
        else:
            print("Invalid type for sex.")

    # Method to update the pet ID
    def update_petID(self, petID):
        if isinstance(petID, str):
            self.petID = petID
        else:
            print("Invalid type for pet ID.")

    # Method to update the owner's name
    def update_owner_name(self, owner_name):
        if isinstance(owner_name, str):
            self.owner_name = owner_name
        else:
            print("Invalid type for owner name.")


# Child class representing a specific type of pet: Dog
class Dog(Pet):
    # Extends Pet class and adds breed and is_trained attributes
    def __init__(self, name, age, sex, petID, owner_name, breed: str, is_trained: bool):
        super().__init__(name, age, sex, petID, owner_name)
        self.breed = breed
        self.is_trained = is_trained

    def print_attributes(self):
        super().print_attributes()  
        print(f"Breed: {self.breed}")
        print(f"Trained: {self.is_trained}")

    # Method to update breed
    def update_breed(self, breed):
        if isinstance(breed, str):
            self.breed = breed
        else:
            print("Invalid type for breed.")

    # Method to update training status
    def update_is_trained(self, is_trained):
        if isinstance(is_trained, bool):
            self.is_trained = is_trained
        else:
            print("Invalid type for is_trained.")


# Create an instance of Pet
pet1 = Pet("Milo", 3, "Male", "P001", "Alice")

# Create an instance of Dog 
dog1 = Dog("Buddy", 5, "Male", "D001", "Bob", "Labrador", True)

# Print attributes of the Pet instance
print("Pet Instance:")
pet1.print_attributes()

# Print attributes of the Dog instance
print("\nDog Instance:")
dog1.print_attributes()

# Update some attributes of pet1 and print them again
print("\nUpdating pet 1...")
pet1.update_age(7)
pet1.update_name("Milo Jr.")
pet1.print_attributes()

# Update some attributes of dog1 and print them again
print("\nUpdating dog 1...")
dog1.update_breed("Golden Retriever")
dog1.update_is_trained(False)
dog1.print_attributes()
