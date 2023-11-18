i=1
s=0
count=0

while i!=0:
    i=int(input("enter i:"))
    if count==0 and i==0 :
        print("Erorr the first")
        break 
    
    s=s+i
    count+=1  # count= count+1
    if i==0:
        print("Average ", s/(count-1))
        break
    
     