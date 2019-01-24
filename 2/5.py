class Person:
    __name=''
    def SetName(self,name):
         self.__name=name
    def GetName(self):
        return self.__name


x=Person()
x.SetName("xiao.xinmiao")
name=x.GetName()
print(name)