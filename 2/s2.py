class Person:
    name =''
    age =0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayHello(self,name,age):
        print("hello everybody,I am {0},I am {1}".format(name,age))

ldh=Person('liu.dehua',18)
zxy=Person('zhang.xueyou',20)
print("liu.dehua info",ldh.name,ldh.age)
print("zhang.xueyou info",zxy.name,zxy.age)

