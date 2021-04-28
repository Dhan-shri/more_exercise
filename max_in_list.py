# Yeh ek list mein andar aur lists hain. Andar waali list mein har bache ke saare subjects mein marks hain. Ek max_marks naam ka function banao jo ki ek aisi list le aur har students ke maximum marks print kare.
#  Jaise agar main aapke max_marks function ko upar waali list ke saath call karunga ,

marks = [[45, 21, 41, 63], [12, 54, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
def max_marks(marks):
    i=0
    while i<len(marks):
        j=0
        k=marks[i][0]
        while j<len(marks[i]):
            if marks[i][j]>k:
                k=marks[i][j]  
                # print(k)  
            j=j+1
        i=i+1
        print(k)
max_marks(marks)
            

            
