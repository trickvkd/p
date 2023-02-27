l=input("enter a striing")
l1=list(l)
for i in l1:
    c=0
    if i!="":
        for j in range(0,len(l1)):
            if(l1[j]==i):
                c=c+1
                l1[j]=""
        print(i,"=",c)
