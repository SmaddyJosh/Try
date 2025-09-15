# Base Class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # private attribute (encapsulation)

    def call(self, contact):
        return f"{self.brand} {self.model} is calling {contact}..."

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"

    def battery_status(self):
        return f"Battery: {self.__battery}%"

# Subclass (Inheritance)
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        # call parent constructor
        super().__init__(brand, model, battery)
        self.camera_megapixels = camera_megapixels

    # Polymorphism: overriding call method
    def call(self, contact):
        return f"Video calling {contact} using {self.camera_megapixels}MP camera 📷"

    def take_photo(self):
        return f"Photo taken with {self.camera_megapixels}MP camera!"

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 50)
phone2 = SmartPhoneWithCamera("Apple", "iPhone 15", 80, 48)

# Using methods
print(phone1.call("Alice"))
print(phone1.charge(30))
print(phone1.battery_status())

print(phone2.call("Bob"))  # overridden method (polymorphism)
print(phone2.take_photo())
print(phone2.battery_status())
