Total=0
while True:
    age=input("Enter the age of the guest (press Enter to finish):")
    if not age:
        break
    f_age=float(age)
    cost=0
    if f_age<=2:
        cost=0
    elif 3<=f_age<=12:
        cost=14.00
    elif f_age>=65:
        cost=18.00
    else:
        cost=23.00
    Total+=cost
print("Total cost: ${:.2f}".format(Total))  
    
    

