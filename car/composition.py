class Key:
    def __init__(self, colour: str, character: str, special_character: bool):
        self.colour = colour
        self.character = character
        self.special_character = special_character

class Keyboard:
    def __init__(self, colour: str, backlit: bool, language: str, numlock: bool, keys: Key):
        self.colour = colour
        self.backlit = backlit
        self.language = language
        self.numlock = numlock
        self.key = keys

class Screen:
    def __init__(self, size: float, touch_screen: bool, type: str):
        self.size = size
        self.touch_screen = touch_screen
        self.type = type


class Battery:
    def __init__(self, capacity: int, type: str):
        self.capacity = capacity
        self.type = type


class Laptop:
    def __init__(self, name: str, model: str, make: str, colour: str, keyboard: Keyboard, screen: Screen, battery: Battery):
        self.name = name
        self.model = model
        self.make = make
        self.colour = colour
        self.keyboard = keyboard
        self.screen = screen
        self.battery = battery

def run():
    dell = Laptop("dell", "Elitebook", "dell", "black", Keyboard("black", True, "English", True, Key("black", "array", ))