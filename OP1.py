class student:
    def __init__(self,firstname,age,course,gender):
        self.firstname = firstname
        self.age = age
        self.course = course
        self.gender = gender

# behaviour
    def study(self):
        print(self.firstname, "is studying")
# object
student1 = student("Joe", 21,"MIT", "male" )
student1.study()
print(student1.gender)
student2 = student("Amina", 31, "Cybersecurity","female")
student2.study()


#

