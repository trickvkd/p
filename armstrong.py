a=int(input("enter a number"))
def armstrong(n):
    s=0
    m=n
    while(n>0):
        r=n%10
        s=(r*r*r)+s
        n=int(n/10)
    if(s==m):
        print("Armstrong")
    else:
        print("Not armstrong")
armstrong(a)
