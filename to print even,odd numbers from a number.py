#from a given number n form 2 numbers
#1.e--with even digits of the number
#2.o--with odd digits of the number

n=int(input('enter a number-'))
e=0
o=0
while n:
    r=n%10
    if r%2==0:
        e=e*10+r
    else :
        o=o*10+r
    n=n//10
print(e,o)

x=0
y=0
while e :
    r=e%10
    x=x*10+r
    e=e//10
print(x)
while o:
    r=o%10
    y=y*10+r
    o=o//10
print(y)

print(x**2+y**2)
