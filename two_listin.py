#Socho aapke paas 2 lists hain.
#  Aapne aisa code likhna hain jisse ek nayi list banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain
list1 = [1, 342, 75, 23,10, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
k=[]
while i<len(list1):
    num=list1[i]
    if num in list2:
        k.append(num)
        k.sort()
    i=i+1
print(k)
