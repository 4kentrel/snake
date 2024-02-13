#Inbuilt functions
number = max(47,55,17,38)
print(number)
num = min(6,34,20,79)
print(num)
z= pow(2,3)
print(z)

#User-defined functions
def name():
    print("Kentrel")
name()#Calling a function
def details():
    name = "Kentrel"
    age = "18"
    course = "MIT"
    print(name,age,course)
details()
#Parameters/variables and arguments
def patients(name,age,gender,status):
    print(name,gender,age,status)
patients("kentrel","18","male","Single")
def multiply(x,y):
    print(x*y)
multiply(43,56)
multiply(98,21)
multiply(9,7)
multiply(5,8)

#Create a user-defined functions
#Called employees.Display the details of five employees using the postition:Name age position salary
def employees(name,age,position,salary):
    print(name,age,position,salary)
employees("John","29","Sales expert","50000ks")
employees("Bruce","27","Finances","80000ks")
employees("Liam","28","Product management","90000ks")
employees("Cole","34","Managing director","150000ks")
employees("Kim","30","Designing","120000ks")