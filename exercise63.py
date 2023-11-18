print("{:<11} {:<11}".format("Celsius", "Fahrenheit"))
for Celsius in range(0,101,10):
    Fahrenheit=32+(9/5)*Celsius
    print("{:<11} {:<11}".format(Celsius, Fahrenheit))

