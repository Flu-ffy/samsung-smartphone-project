# Base class for a smartphone
class Smartphone:
    def __init__(self, brand, model, storage, color, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.price = price

    def display_specs(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nStorage: {self.storage}GB\nColor: {self.color}\nPrice: ${self.price}"

    def make_call(self, phone_number):
        return f"Calling {phone_number}..."

    def take_photo(self):
        return "Taking a photo..."

# Derived class for a Samsung smartphone
class SamsungSmartphone(Smartphone):
    def __init__(self, model, storage, color, price, camera_quality, battery_life):
        # Initializing parent class with specific attributes
        super().__init__("Samsung", model, storage, color, price)
        self.camera_quality = camera_quality
        self.battery_life = battery_life

    # Overriding the display_specs method to add camera and battery details
    def display_specs(self):
        base_specs = super().display_specs()
        return f"{base_specs}\nCamera Quality: {self.camera_quality}MP\nBattery Life: {self.battery_life} hours"

    def use_fingerprint_unlock(self):
        return "Unlocking with fingerprint..."

    def fast_charging(self):
        return "Charging with fast charger..."

# Creating a Samsung smartphone object
samsung_galaxy_s21 = SamsungSmartphone("Galaxy S21", 128, "Phantom Black", 799, 108, 24)

# Displaying the details of the Samsung Galaxy S21
print(samsung_galaxy_s21.display_specs())
print(samsung_galaxy_s21.make_call("123-456-7890"))
print(samsung_galaxy_s21.take_photo())
print(samsung_galaxy_s21.use_fingerprint_unlock())
print(samsung_galaxy_s21.fast_charging())
