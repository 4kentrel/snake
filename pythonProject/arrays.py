courses = ["MIT","Cybersecurity","Datascience"]
print(courses[1])

#Accessing an element in an array

#Looping through an array
for course in  courses:
    print(course)

#Adding a new element into an array

courses.append("Android programming")
print(courses)

#Deleting an element from an array
courses.remove("Datascience")
print(courses)
