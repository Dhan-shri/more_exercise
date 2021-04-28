# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai") 

pass_word=input("enter a passward")
if len(pass_word)>=6 or len(pass_word)<=16:
    if "$" in pass_word:
        if "2" or "8" in pass_word:
            if "A" or "Z" in pass_word:
                print("it is strong password")
            else:
                print("it is weak password")
        else:
            print("it is not a strong passward")
    else:
        print("strong passward must contain $ symbol")
else:
    print("strong passward must contain 6 to 16 character")