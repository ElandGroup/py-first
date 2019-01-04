rows =13
mid=int(rows/2)

for row in range(rows):
    if row <=mid:
        for blank in range(mid-row):
            print(" ",end="")
        for star in range(2*row+1):
            print("*",end="")
    else:
        for blank in range(row-mid):
            print(" ",end="")
        for star in range(rows-2*(row-mid)):
            print("*",end="")
    print("")
