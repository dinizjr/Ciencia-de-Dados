class Person(object):

    def __init__(self, full_nome):
        self.__full_name = full_name#private

    def __str__(self):#to string
        return self.__full_name

    @property
    def __full_name(self, value):
        return self.name + '' + self.surname

    @__full_name.setter
    def __full_name(self, value):
        return self




p = Person('Data Science Facens'
print(p.name)
print()