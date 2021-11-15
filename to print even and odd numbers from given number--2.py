#to print even and odd number from a given number-2nd way
z=int(input('enter a number-'))
n=0
while z:
    r=z%10
    n=n*10+r
    z=z//10
print(n)
e=0
o=0
while n:
    r=n%10
    if r%2==0:
        e=e*10+r
    else:
        o=o*10+r
    n=n//10
print(e,o)
    
