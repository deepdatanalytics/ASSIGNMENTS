# class Employee:
    
#     raise_amnt = 1.04   #class attribute oldu. Objeleri de kapsıyor dolayısıyla.

#     def __init__(self,firstname,lastname,email,pay):

#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.pay = pay

#     def fullname(self):

#         return "{} {}".format(self.firstname, self.lastname)

#     def apply_raise(self):

#         self.pay = int(self.pay * self.raise_amnt)

#     @classmethod
#     def set_raise_amnt(cls,amount):
#         cls.raise_amnt = amount


# emp_1 = Employee("Martin","Lane","martin.lane@clarus.com",4000) #Instance alma. Yani obje oluşturma. 

# print(emp_1.firstname)
# print(emp_1.lastname)
# print(emp_1.email)

# print(emp_1.fullname())  #

# print(emp_1.raise_amnt)
# print(Employee.raise_amnt)

# Employee.raise_amnt = 1.06

# print(emp_1.raise_amnt)
# print(Employee.raise_amnt)

# emp_1.raise_amnt = 1.07

# print(emp_1.raise_amnt)
# print(Employee.raise_amnt)                                         #Class Var ve Obj var iki farklı kavram var.

# Employee.raise_amnt = 1.08

# print(emp_1.raise_amnt)
# print(Employee.raise_amnt)

# emp_2 = Employee("Martin2","Lane2","mart@daf.com",5000)

# print(emp_1.raise_amnt)
# print(emp_2.raise_amnt)
# print(Employee.raise_amnt)

# print(emp_1.__dict__)
# print(emp_2.__dict__)


# print(emp_1.pay)
# print(emp_2.pay)


### Class Metodlar ve 

# emp_1 = Employee("Martin","Lane","martin@clarusway.com",4000)
# emp_2 = Employee("Martin2","Lane","lane@clarus.com",5000)

# Employee.set_raise_amnt(1.10)

# print(Employee.raise_amnt)
# print(emp_2.raise_amnt)

# Employee.raise_amnt = 2

# print(Employee.raise_amnt)
# print(emp_2.raise_amnt)


class Employee:
    
    raise_amnt = 1.04   #class attribute oldu. Objeleri de kapsıyor dolayısıyla.

    def __init__(self,firstname,lastname,email,pay):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.pay = pay

    def fullname(self):

        return "{} {}".format(self.firstname, self.lastname)

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amnt)

    @classmethod
    def set_raise_amnt(cls,amount):
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls,emp_str):
        firstname, lastname, email, pay = emp_str.split("-")
        return cls(firstname, lastname, email, pay)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True

# emp_str_1 = "Martin-Lane-martin@clarus.com-5000"

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)

# new_emp_1_1 = Employee(new_emp_1.firstname, new_emp_1.lastname, new_emp_1.email, new_emp_1.pay)

# print(new_emp_1_1.email)


#########################    STATIC METHOD    ###################################

import datetime
my_date = datetime.date(2020,8,8)

print(Employee.is_workday(my_date))