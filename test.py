num=2
print(num % 2==False)
print(num % 2==0)

x = 7
i = 1

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 3
    else:
        x = 7 * (i+1)
    i += 1

if flag == 3:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
