import math 
def TRI(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt((s*(s-a)(s-b)(s-c)))
    print("the semiperimeter of triangle =",s);
    print("the area of triangle =",area)
def rec(w,h):
    print("the area of a rectangle=",w*h)
def cir(r):
    print("the area of circle: ",math.pi*r*r)
def squ(a):
    print("the area of square=",a*a)
a = int(input("enter a value :"))
b = int(input("enter b value :"))
c = int(input("enter c value :"))
w = int(input("enter w value :"))
h = int(input("enter h value :"))
r = int(input("enter r value :"))
TRI(a,b,c)
rec(w,h)
cir(r)
squ(a)
