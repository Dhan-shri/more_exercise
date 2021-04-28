#Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain.
#  Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. 


string_list = ["Rishabh", "Rishabh", "Abhishek","Abhishek", "Rishabh","Divyashish", "Abhishek","Divyashish"] 
i=0
k=[]
while i<len(string_list):
    string=string_list[i]
    k.append(string)
    j=1
    while j<len(string_list):
        s=string_list[j]
        if string in s:
            del string_list[j]
        j=j+1
    i=i+1
print(k)

# string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 
# i=0
# k=[]
# while i<len(string_list):
#     string=string_list[i]
#     k.append(string)
#     j=1
#     while j<len(string_list):
#         s=string_list[j]
#         if string in s:
#             del string_list[j]
#         j=j+1
#     i=i+1
# print(k)