class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        if(self.age<18):
            print("%s est mineur"%(self.name))
        else:
            print("%s est majeur"%self.name)


"""
p1 = Person("John", 36)
print(p1.name)
p2=Person("Alaa",17)
p2.test()
p1.test()
"""


