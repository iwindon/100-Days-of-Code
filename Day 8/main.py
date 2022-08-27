def greet():
    print("Hello")
    print("My name is HAL")
    print("How are you doing today?")

greet()

#Function that allows input

def greet_with_name(name):
    print(f"Hello {name}")
    print("My name is HAL")
    print("How are you doing today?")

greet_with_name("Ivan")

# Functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You live in {location}")

greet_with("Ivan","North Carolina")

greet_with(location="North Carolina", name="Ivan Windon")
