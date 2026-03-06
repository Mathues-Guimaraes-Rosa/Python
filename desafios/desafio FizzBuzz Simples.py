a = int(input('digite um numero: '))

if(a %5 ==0 and a %3 == 0):
    print('FizzBuzz')
elif (a %3 == 0):
    print('Fizz')
elif(a %5 == 0):
    print('Buzz')
else:
    print(f'impossivel{a}')    