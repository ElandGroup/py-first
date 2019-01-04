rows =15
mid=int(rows/2)

for row in range(rows):
    if row <=mid:
        print((mid-row)*" ",end="*"*(2*row+1))
        print()
    else:
        print((row-mid)*" ",end="*"*(rows-2*(row-mid)))
        print()


for row in range(1,2*rows+1):
    if row <=rows-1:
        print((rows-row)*" ",end="* "*(row))
        print()
    else:
        print((row-rows)*" ",end="* "*(2*rows-row))
        print()
