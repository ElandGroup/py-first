class Person:
    name=''
    def __init__(self,name):
        self.name=name

x=Person("xiao.xinmiao")
print(x.name)

class Person2:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name 
        self.age =age

y=Person2("liu.ruoying",18)
print(y.name)
