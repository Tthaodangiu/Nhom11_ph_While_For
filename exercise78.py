#Đổi từ thập phân qua nhị phân
decimal = int(input("Enter a decimal (base 10)   "))
result = ""

while decimal > 0:
    remainder = decimal % 2
    result = str(remainder) + result
    decimal = decimal // 2

print("The binary number is", result)