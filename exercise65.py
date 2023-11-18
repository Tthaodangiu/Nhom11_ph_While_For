#Tính đa giác vecto
import math
sum = 0
x = str(input("Enter the x part of the coordinate: (blank to quit): "))
while True:
    if x != "":
        x = int(x)
        y = int(input("Enter the y part of the coordinate: "))
        p1 = x
        p2 = y
        temp1 = x
        temp2 = y
        x = str(input("Enter the x part of the coordinate: (blank to quit): "))
        while x != "":
            x = int(x)
            y = int(input("Enter the y part of the coordinate: "))
            dist = math.sqrt((x - temp1)*(x - temp1) + (y - temp2)*(y - temp2))
            sum = sum + dist
            temp1 = x
            temp2 = y
            x = str(input("Enter the x part of the coordinate: (blank to quit): "))
        else:
            dist = math.sqrt((temp1 - p1)*(temp1 - p1) + (temp2 - p2)*(temp2 - p2))
            sum = sum + dist
        print('The perimeter of that polygon is:',sum)
    else:
        break