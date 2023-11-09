import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error: division by zero'
    return x / y

def square_root(x):
    if x < 0:
        return 'Error: unable to extract the square root of a negative number'
    return math.sqrt(x)
def fibonacci(x):
    if x in (1, 2):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

def main():
    while True:
        print('Choose an operation:')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Square Root')
        print('6. Fibonacci number')
        print('7. Exit the calculator')

        choice = input('Enter the operation number: ')

        if choice == '7':
            print()
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print('Incorrect choice of operation. Please try again.')
            continue

        try:
            num1 = float(input('Enter the first number: '))
            num2 = None

            if choice != '5' and choice != '6':
                num2 = float(input('Enter the second number: '))
        except ValueError:
            print('You entered a string, please enter a number to continue using the calculator.')
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = square_root(num1)
        elif choice == '6':
            result = fibonacci(num1)

        print(f'Result: {result}')

if __name__ == '__main__':
    main()
