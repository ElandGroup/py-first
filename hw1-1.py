rows =13
mid=int(rows/2)

def printStr(num,param):
    for i in range(num):
        print(param,end="")


for row in range(rows):
    if row <=mid:
        printStr(mid-row," ")
        printStr(2*row+1,"*")
        print()
    else:
        printStr(row-mid," ")
        printStr(rows-2*(row-mid),"*")
        print()