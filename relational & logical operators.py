n=int(input('enter a roll number-'))
p=int(input('enter marks in physics-'))
c=int(input('enter marks in chemisty-'))
s=int(input('enter marks in computer science-'))
t=(p+c+s)
d=(t/3)
print('roll number-',n)
print('total marks-',p+c+s)
print('percentage-',t/3)
if d>=80:
    print('division-first')
elif d==70<=d<=79:
    print('division-second')
elif d==60<=d<=69:
    print('division-third')
elif d==50<=d<=59:
    print('division-fourth')
else:
    print('division-fail')
