a=int(input("enter a number:"))
b=int(input("enter a number:"))
count=0
while(a<=b):
    for i in range(a,b+1):
        if(a%i==0):
            count=count+1
        if(count==2):
            print(a)
        a=a+1
