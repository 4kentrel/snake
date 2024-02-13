# Data type
number = 69 # int
num = 47.54 # float
greeting = ("Hello there") #string or str
isPythoninteresting = True #boolean or bool
# A variable storing multiple values
languages = [ "Python","Javascript","PHP"] #list
fruits = ("apple","banana","orange")#tuple
countries = {"Kenya","Bangladesh","Utopia"}
#Dictionary

details = {
    "firstname":"Brian",
    "age" : 18,
    "course" : "MIT",
    "nationality" :"Kenyan"
}
print(number)
print(isPythoninteresting)
print(languages)
print(countries)
print(details)
print(details["age"])


# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# Typecasting - converting one data type to another
print(float(number))
print(int(number))