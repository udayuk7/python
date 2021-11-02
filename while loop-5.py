#printing even numbers in a given range
a=int(input('enter a value-'))
b=int(input('enter a value-'))
while(a<=b):
    if a%2==0:
        print(a,end=' ')
    a+=1
