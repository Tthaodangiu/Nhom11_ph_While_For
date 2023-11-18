#Đổi từ nhị phân qua thập phân
bi=str(input("Enter a binary (base 2):"))
n=len(bi) - 1
dec=0
for x in bi:
        a=int(x)
        dec = dec + (a*(2**n))
        n = n-1
print("The decimal number is:",dec)