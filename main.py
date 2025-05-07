class Pet():
    def __init__(self, pet_name):
        self.name = pet_name
        self.age = 0
        self.hunger = 5
        self.boredom = 3
        self.sleepiness = 3
        self.dead = False

    def pretty_print(self):
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")
      print(f"Hunger: {self.hunger}")
      print(f"Boredom: {self.boredom}")
      print(f"Sleepiness: {self.sleepiness}")
      print(f"Dead? {self.dead}")
      print()

pet1 = Pet("Tinkles")
pet1.pretty_print()