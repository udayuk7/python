#write a python program to print all the 3 or 5 multiples in the given range
a=int(input('enter a number-'))#5
b=int(input('enter a number-'))#10
while (a<=b): 
    if a%3==0 or a%5==0 : 
        print(a,end=' ') 
    a+=1
        
