text = input("Enter the text you want to encode: ") 
k = int(input("Enter the shift amount: ")) 
result = ""
for i in range(len(text)):
    char = text[i]
    if "A"<=char<="Z": #Chữ in hoa
        result = result + chr((ord(char) + k-65) % 26 + 65) 
    elif 97<=ord(char)<=122: #Chữ thường
        result = result + chr((ord(char) + k - 97) % 26 + 97)
    else:
        result = result + char
print(result)