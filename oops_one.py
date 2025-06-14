# # ----oops tell about class & objects--------
# class: class is a blueprint or a template. eg. form for a exam that conatins name,age,electives,fathersname
# objects : specific instance created from the template (class). Eg. form which conatins data from john doe

class Employee:
    company = "Hp"
                            # this is class
    def get_salary(self):
        return 34000
    
e = Employee()      #An object of class Employee is created here
print(e.get_salary())   #Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())
print(e2.company)


# ----------------------------------------


# -----constructors- use constructors to initialize our objects-----

class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary #creat an instance attribute of name salary and assignit with it salary
        self.name = name
        self.bond = bond

    def get_salary(self): #self is important here because self a way to reference the object of the class which is ebing created
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. salary is {self.salary}.the bond is for {self.bond}years")
    
e1 = Employee(34000,"john doe",4)
# print(e1.get_salary())

e1.get_info()

# ---------