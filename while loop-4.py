#take 2 numbers from user and print numbers in backward in a given range
a=int(input('enter a value-'))
b=int(input('enter a value-'))
while(a>=b):
    print(a,end=' ')
    a-=1
while(b>=a):
    print(b,end=' ')
    b-=1
    
