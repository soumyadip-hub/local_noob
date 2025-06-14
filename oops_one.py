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


