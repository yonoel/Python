class Person(object):
    __slots__ = ('name')
    def __init__(self):
        pass

    def __init__(self,name="name",age=0,sex="male"):
        self.name = name
        self.age = age
        self.__sex = sex

    def introduce(self):
        print("my name is %s and age is %d" % (self.name,self.age))

    def toJson(self):
        return '''"{"name":"%s","age":"%d"}"'''%(self.name,self.age)





try:
    persona = Person("name_aa", 15, "male")
    persona.name = "name_aaa"
    persona.age = 20
except AttributeError as e:
    print("has error",e)
else :
    print("hehe")

personb = Person()
persona.introduce()
personb.introduce()

def fn1():
    print("hehe")
    pass

personb.fn = fn1

personb.fn()