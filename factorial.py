# Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska factorial print karega. 
# Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 print karega aur aise hi dusre numbers ke lie. Note: Abhi ke liye yeh soch lo ki user sirf positive integers hi dalega. Negative integers kabhi nahi dalega.
n=int(input("enter a number"))
i=1
a=1
while i<=n:
    a=a*i
    i=i+1
print(a)