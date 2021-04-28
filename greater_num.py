#input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo 
# Note: Isme aap loops ka use nahi kar sakte.

a=int(input("a:-"))
b=int(input("b :-"))
c=int(input("c :-"))
if a>b and a>c:
    print("the maximum number is",a)
elif b>a and b>c:
    print("the maximim number is",b)
else:
    print("the maximum number is ",c)