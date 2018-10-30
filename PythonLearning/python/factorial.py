n = int(input('Enter number: '))
fact = 1
if n < 0:
    print('Factorial not possible')
elif n == 0:
    print('1')
else:
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
