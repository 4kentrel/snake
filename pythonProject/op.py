class person:
    def __init__(self,first_name,age,gender,):
        self.first_name =first_name
        self.age =age
        self.gender =gender
    def details(self):
        print(self.first_name, "is typing")
teacher = person("John","24","Male")
accountant = person("Mj","21","Female")
doctor = person("James","39","Male")
print(teacher.first_name,teacher.age,teacher.gender)
print(accountant.first_name,accountant.age,accountant.gender)
print(doctor.first_name,doctor.age,doctor.gender)
accountant.details()