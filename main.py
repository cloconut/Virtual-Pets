class Pet: #defining pet class
  def __init__(self, pet_name):
    #default values
    self.name = pet_name
    self.age = 0
    self.hunger = 5
    self.boredom = 3
    self.sleepiness = 3
    self.dead = False

  def __str__(self):
    string = f"""Name: {self.name}
Age: {str(self.age)}
Hunger: {str(self.hunger)}
Boredom: {str(self.boredom)}
Sleepiness: {str(self.sleepiness)}
Dead? {str(self.dead)}
"""
    return string

    def feed(self):
        if self.dead:
         return
        self.hunger = self.hunger - 3
        if self.hunger < 0:
         self.hunger = 0

    def play(self):
        if self.dead:
         return
     self.boredom = self.boredom - 3
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
     if self.dead:
         return
        self.sleepiness = self.sleepiness - 3
     if self.sleepiness < 0:
            self.sleepiness = 0

  #def wait(self):

action = input("What do you want to do with your pet? ")

while action != "":
  #put the if statement here
  print("-----------------------------------------------------")
  print(pet1)
  print("-----------------------------------------------------")
  action = input("What do you want to do with your pet? ")


if action == "feed":
    pet.feed()
    #make time pass
    #pet.wait()
  #fill in the if statement for the rest of the actions with elifs

if action == "play":
    pet.play()
    #make time pass
    #pet.wait()
  #fill in the if statement for the rest of the actions with elifs
 
  #sleep
if action == "sleep":
    pet.sleep()
    #make time pass
    #pet.wait()
  #fill in the if statement for the rest of the actions with elifs  
  
  #wait

else:
    print("You can only choose to feed, play, sleep or wait. ")

pet1 = Pet("stinker")
print(pet1)