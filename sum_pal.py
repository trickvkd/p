n=int(input("Enter a number"))
def s_p(n):
    m=0
    s=0
    p=n
    while(n>0):
        r=n%10
        s=s+r
        m=(m*10)+r
        n=int(n/10)
    print("sum of digits:",s)
    print("reverse of the number:",m)
    if p==m:
        print("Number is palindrome")
    else:
        print("Not palindrome")
s_p(n)
