# blueprint
class animal:
    def __init__(self,type,hasScales,hasWings,color):
        self.type = type
        self.hasScales = hasScales
        self.hasWings = hasWings
        self.color = color
    def movement(self):
        print(self.type, "is moving")

# object
animal1 = animal("fish", True,True, "grey")
print(animal1.color)
animal1.movement()
animal2 = animal("lion", False,False, "brown" )
print(animal2.color)
animal2.movement()
animal3 = animal("bird", True,True, "Black" )
print(animal3.color)
animal3.movement()