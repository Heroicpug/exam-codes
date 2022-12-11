n = int(input("enter the number of disks :"))
A=[]
B=[]
C=[]
for k in range(n):
    A.append(n-k)
    print("k value=",k)
    print("n-k value=",n-k)
print(A,B,C)
def Tower2(n,frmA,toC,auxB):
    if n==1:
        toC.append(frmA.pop())
        print(A,B,C)
        return
    Tower2(n-1,frmA,auxB,toC)
    toC.append(frmA.pop())
    print(A,B,C)
    Tower2(n-1,auxB,toC,frmA)
Tower2(n,A,C,B)
