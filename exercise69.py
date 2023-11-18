pi=3
sign=1
for i in range(1,16):
    denominator=2*i*(2*i+1)*(2*i+2)
    fraction=4/denominator
    pi=pi+sign*fraction
    sign=sign*-1
    print("Approximations of pi",i,":",round(pi,10))
    
