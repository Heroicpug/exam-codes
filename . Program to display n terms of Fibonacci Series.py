def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n = int(input("enter the positive number of terms :"))
print("fibonacci series are :")
for i in range (0,n):
    print(fib(i))
