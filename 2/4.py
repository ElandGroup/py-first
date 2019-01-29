class Person:
    __name=''
    def GetName(self):
        return self.__name
    def __init__(self,name):
        self.__name=name

x=Person("xiao.xinmiao")
print(x.GetName())

class Person2:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name 
        self.age =age

y=Person2("liu.ruoying",18)
print(y.name)
