"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SmartDevice:
    # Class namespace (shared by all instances)
    category = "Smart Home Tech"

    def __init__(self, name, features):
        # Instance namespace (unique to each object)
        self.name = name
        self.features = features

    def display_info(self):
        print(f"Device: {self.name} | Features: {self.features}")
    pass


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SecurityCamera(SmartDevice):
    # New class variable
    device_type = "Camera"

    def __init__(self, name, features, resolution, brand):
        super().__init__(name, features) # Inherent from parent
        self.resolution = resolution
        self.brand = brand

    # Override method from parent
    def display_info(self):
        print(f"Camera: {self.name} | Brand: {self.brand} | Res: {self.resolution} | Features: {self.features}")
    pass


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    cam1 = SecurityCamera("Front Door", ["Night Vision"], "1080p", "Ring")
    cam2 = SecurityCamera("Backyard", ["Motion Alert"], "4K", "Nest")

    print(f"Class variable via Class: {SecurityCamera.category}")

    print(f"Class variable via Object: {cam1.category}")

    cam1.battery_life = "6 months"

    print(f"\ncam1 __dict__: {cam1.__dict__}")
    print(f"cam2 __dict__: {cam2. __dict__}")

    print(f"\nSecurityCamera Class __dict__ keys: {list(SecurityCamera.__dict__.keys())}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original_cam = SecurityCamera("Garage", ["Video", ["Night Vision", "Infrared"]], "1080p", "Arlo")

    # Shallow copy
    shallow_cam = copy(original_cam)

    # deep copy
    deep_cam = deepcopy(original_cam)

    original_cam.features[1].append("Color Night Vision")

    print(f"Original Nested Features: {original_cam.features}")
    print(f"Shallow Copy Features: {shallow_cam.features}")
    print(f"Deep Copy Features: {deep_cam.features}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Testing Parent Object ---")
    # one object from the parent class
    basic_device = SmartDevice("Smart Plug", ["Remote Control"])
    basic_device.display_info()

    print("\n--- Testing Child Object ---")
    # one object from the child class
    my_cam = SecurityCamera("Driveway Cam", ["Night Vision"], "4K", "Wyze")

    # inheritance by calling methods
    my_cam.display_info()

    # Call demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()