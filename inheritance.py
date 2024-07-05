# parent class and child class
class animal:
     def speak(self):
         print("animal is speaking")
     def movement(self):
         print("animal is moving")
 # child class
class duck(animal):
     def quack(self):
         print("duck is quacking")

class bee(animal):
    def buzz(self):
        print("bee is buzzing")
a = animal()
a.movement()
b = duck()

c = bee()