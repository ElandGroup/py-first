class Person:
    name=''
    def sayHello(self,msg):
        return self.name+' say:'+msg
x =Person()
x.name="xiao.xinmiao"
hello =x.sayHello("good morning.")
print(hello)


y =Person()
y.name="liu.ruoying"
hello2 =y.sayHello("good everning.")
print(hello2)