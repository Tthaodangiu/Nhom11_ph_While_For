Total=0
while True:
    pr=input("Please enter the price (press enter to finish):")
    if not pr:
        break
    Total+=float(pr)
print("The total cost of all the entered items:$",Total,sep="")
pennies_needed=Total*100
remainder=pennies_needed%5
if remainder<2.5:
    ad_total=pennies_needed - remainder
else:
    ad_total=pennies_needed+(5-remainder)
ad_total_dollar=ad_total/100
cash_payment=round(ad_total_dollar/5)*5
print("Cash payment:$",cash_payment,sep="")
    
