# lst=[1,2,3,4,5,6,7,8,9,10]
lst=[2,4,6,8]
i=1
n=lst[0]
k=[]
while i<len(lst):
    s=lst[i]
    j=s-n
    k.append(j)
    n=s
    i=i+1
print(k)


