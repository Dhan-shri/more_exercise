#Ab aapko nayi list banani hai jisme dono lists ke elements hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone chaiye. 
# Agar humare paas yeh do lists hain:
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16,18] 
i=0
k=[]
while i<len(list1):
    j=0
    while j<len(list2):
        num=list2[j]
        if num not in list1:
            list1.append(list2[j])
        j=j+1
    i=i+1
list1.sort()
print(list1)
            










