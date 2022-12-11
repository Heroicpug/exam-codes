n = int(input("Enter the number of subject marks: "))
tot = 0
for i in range(1,n+1):
    print("Enter the ",str(i),"mark :")
    m = int(input())
    tot = int(tot)+m
    print ("total marks =",tot)
    avg = tot/n
print("average of marks",avg)
if avg >=80:
    print("grade A")
elif avg>=70 and avg<80:
    print("grade B")
elif avg>=60 and avg<70:
    print("grade c")
elif avg>=40 and avg<60:
    print("grade D")
elif avg<40 :
    print("grade E")
else:
    print("fail")
