list1=[1,2,3,4]
list2=[5,8,6,7]
def list_c():
    for i in list1:
        for j in list2:
            if(i==j):
                return("true")
if(list_c()=="true"):
    print("It have common values")
else:
    print("no common values")
