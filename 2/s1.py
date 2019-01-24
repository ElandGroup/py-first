z_name ='liu.dehua'
z_age =18

x_name ='zhang.xueyou'
x_age =20

def SayHello(name,age):
    print("hello everybody,I am {0},I am {1}".format(name,age))

#正确的逻辑 和 代码
SayHello(z_name,z_age)
SayHello(x_name,x_age)
#很容易 写出下面错误的代码么
SayHello(x_name,z_age)
