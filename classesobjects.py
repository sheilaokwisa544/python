# a class is a blueprint of an object must have a behaviour
# objects is an instance of a class
# a method is followed by brackets
# class creation
class person:
    # these are properties/attributes/characteristics/variable
    name = "Morris"
    age = 21
    gender ="male"
    def walk(self):
        # behaviour is also a function
        print("person is walking")
# object
person1 = person()
print(person1.name)
print(person1.age)
print(person1.gender)
person1.walk()



