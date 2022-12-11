string= input("Enter the string :")
lower = upper = other = 0
for letter in string:
    if(letter.islower()):
        lower= lower+1
    elif(letter.isupper()):
        upper=upper+1
    else:
        other=other+1
    print("original string",string)
    print("no.of uppercase character :",upper)
    print("no.of lowercase character :",lower)
