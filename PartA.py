class Pet:
    def __init__(self, name: str, age: int, sex: str, petID: str, owner_name: str):
        self.name = name
        self.age = age
        self.sex = sex
        self.petID = petID
        self.owner_name = owner_name

    def print_attributes(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Pet ID: {self.petID}")
        print(f"Owner Name: {self.owner_name}")

    def update_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Invalid type for name.")

    def update_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            print("Invalid type for age.")

    def update_sex(self, sex):
        if isinstance(sex, str):
            self.sex = sex
        else:
            print("Invalid type for sex.")

    def update_petID(self, petID):
        if isinstance(petID, str):
            self.petID = petID
        else:
            print("Invalid type for pet ID.")

    def update_owner_name(self, owner_name):
        if isinstance(owner_name, str):
            self.owner_name = owner_name
        else:
            print("Invalid type for owner name.")


# Child class: Dog (a type of Pet)
class Dog(Pet):
    def __init__(self, name, age, sex, petID, owner_name, breed: str, is_trained: bool):
        super().__init__(name, age, sex, petID, owner_name)
        self.breed = breed
        self.is_trained = is_trained

    def print_attributes(self):
        super().print_attributes()
        print(f"Breed: {self.breed}")
        print(f"Trained: {self.is_trained}")

    def update_breed(self, breed):
        if isinstance(breed, str):
            self.breed = breed
        else:
            print("Invalid type for breed.")

    def update_is_trained(self, is_trained):
        if isinstance(is_trained, bool):
            self.is_trained = is_trained
        else:
            print("Invalid type for is_trained.")


# A8: Create instances
pet1 = Pet("Milo", 3, "Male", "P001", "Alice")
dog1 = Dog("Buddy", 5, "Male", "D001", "Bob", "Labrador", True)

# A9: Print attributes
print("Pet Instance:")
pet1.print_attributes()

print("\nDog Instance:")
dog1.print_attributes()

# A10: Update examples
print("\nUpdating pet 1...")
pet1.update_age(4)
pet1.update_name("Milo Jr.")
pet1.print_attributes()

print("\nUpdating dog 1...")
dog1.update_breed("Golden Retriever")
dog1.update_is_trained(False)
dog1.print_attributes()
