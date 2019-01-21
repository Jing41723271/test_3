import numpy 


i=0
l=[0,10,32,55,21,38,89,10000,273]
def sort(l):
   for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]> l[j]:
                t = l[i]
                l[i]=l[j]
                l[j]=t
sort(l)


print(l)










