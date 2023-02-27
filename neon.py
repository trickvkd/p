def neon():    
    a=int(input("Enter a number"))
    s=a*a
    d=0
    while(s>0):
        r=s%10
        d=d+r
        s=(s/10)
    if(d==a):
            print(a,"is a neon number")
    else:
            print(a,"is not a neon number")
neon()
