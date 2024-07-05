# inbuilt functions / standard library functions
number= max(56, 78, 100) # determines the largest number
print(number)
number= min(56, 78, 100)
print("the min value is", number)

# user defined functions

def name ():
    print("sheila")
name()
# calling a function

def student():
    firstname ="Mark"
    course = "MIT"
    age = "24"
    print(firstname,course,age)
student()

# parameters and arguments # parameter=variable arguments=passed while calling the function/values
def add (num1,num2):
    print(num1 + num2)

add(10,12)


def employee( fullname, age, salary, position, maritalstatus ):
    print(fullname, age, salary, position, maritalstatus)
employee("Mary Muthoni", 56, 450000, "receptionist", "single")
employee("James Kamau", 56, 40000, "manager", "married")

def product(x,y):
    print(x * y)
product(12, 12)

