# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on...")


# Derived Class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage, os):
        super().__init__(brand, model)  # call parent constructor
        self.__storage = storage        # encapsulated attribute
        self.os = os

    # Getter
    def get_storage(self):
        return self.__storage

    # Setter
    def set_storage(self, storage):
        self.__storage = storage

    # Extra method
    def take_photo(self):
        print(f"{self.brand} {self.model} is taking a photo 📸")

    # Overridden method (Polymorphism)
    def power_on(self):
        print(f"{self.brand} {self.model} (Smartphone) is booting into {self.os}...")


# Test
phone1 = Smartphone("Samsung", "Galaxy S24", 256, "Android")
phone1.power_on()
phone1.take_photo()
print("Storage:", phone1.get_storage(), "GB")

phone2 = Smartphone("Apple", "iPhone 15", 512, "iOS")
phone2.power_on()
