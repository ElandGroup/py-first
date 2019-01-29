class person:
    name=''
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print("%s 说:我是抽象的" %(self.name))

class student(person):
    def sayHi(self):
        print("%s 说:老师好！"%(self.name))

class techer(person):
    def sayHi(self):
        print("%s 说:同学们好!"%(self.name))

# def sayHi(person):
#     person.sayHi()

def sayHi(p):
    if isinstance(p,student):
        p.sayHi()
    elif isinstance(p,techer):
        p.sayHi()

sayHi(student("liudehua"))
sayHi(techer("zhangxueyou"))
