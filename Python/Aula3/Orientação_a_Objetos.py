from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):#construtor
        self.name = name #propriedade
        self.salary = salary

    @abstractmethod
    def bonus(self): #Abstrato
        pass #indica que essa função não tem nada escrita

class Operator(Employee):
    def bonus(self):
        return self.salary / 2 # 1000/2

class Manager(Operator):
    def bonus(self):
        return super().bonus() / 3 + self.salary / 2 #bonus do operador / 3 mais o salario do manager / 2#3000/2/3 + 3000/2

class Director(Manager):
    def bonus(self):
        return super().bonus() * 2 #(10000/2/3 + 10000 / 2) * 2

employees  = [Operator('Func Operador', 1000),
              Manager('Func Manager', 3000),
              Director('Func Director', 10000)]

def listBonus(emp):
    for e in emp:
        print(e.bonus())

listBonus(employees)