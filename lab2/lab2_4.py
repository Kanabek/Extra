a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter third number: ')
if b < a and c < a:
    print(a)
elif a < b and c < b:
    print(b)
else:
    print(c)