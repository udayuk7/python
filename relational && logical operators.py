i=int(input('enter id'))
u=int(input('enter units consumed'))
print('user id-',i)
print('units consumed-',u)
if u<=199 :
    c=print('amount charges-',u*1.20)
elif u>=200 and u<400 :
    c=print('amount charges-',u*1.50)
elif u>=400 and u<600 :
    c=print('amount charges-',u*1.80)
elif u>=600 :
    c=print('amount charges-',u*2)
elif c>400:
    print('amount charges-',0.15*c)
