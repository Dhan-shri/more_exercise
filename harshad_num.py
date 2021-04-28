# Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain.
#  Dhang se divide hone ka matlab ki remainder 0 aata hai. Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai Aise hi 18, 21 aur 24 bhi harshad number hai kyunki 1 + 8 = 9 aur 18 ko 9 se divide kar ke remainder 0 hai. Aise hi 1, 2, 3, 4, 5, 6, 7, 8, 9 saare harshad number hain kyunki inki digits ka sum khud yeh number hain aur yeh apne aap se divide ho jate hain. Ek number ke digits nikalne ka code yeh hai:


# def is_harshad_number(num):
#     num_digits=list(str(num))
#     i=0
#     sum=0
#     while i<len(num_digits):
#         n=int(num_digits[i])
#         sum=sum+n
#         i=i+1
#     if num%sum==0:
#         print("it is harshad number")
#     else:
#         print("it is not a harshad number")

# is_harshad_number(21)


def harshad_number(limit):
    i=1
    while i<limit:
        num=list(str(i))
        j=0
        sum=0
        while j<len(num):
            n=int(num[j])
            sum=sum+n
            j=j+1
        if i%sum==0:
            print(i)
        i=i+1

harshad_number(100)
        

