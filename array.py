courses = ["MIT", "cybersecurity", "datascience"]
print(courses)

# adding a new element in an array
# append adds a new element
courses.append("python")
print(courses)

# deleting an element
# remove is used
courses.remove("datascience")
print(courses)

# Accessing an element in an array
print(courses[1])

# looping through an array
for course in courses:
    print(course)

# lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[2])
for x in mylist:
    print(x)

mylist.sort()
print(mylist)
mylist.copy()
print(mylist)