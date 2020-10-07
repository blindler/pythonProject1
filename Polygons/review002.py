print('1. Add two numbers')
print('2. Print your name')
print('3. Quit')

user_input = int(input('Enter an option'))

while user_input != 3:
    if user_input == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        answer = num1 + num2
        print(num1, '+', num2, " = ", answer)

    if user_input == 2:
        name = input("Enter your name: ")
        print("hello,", name)

    user_input = int(input('Enter an option'))

    # if user_input == 3:
    print("goodbye")

print("********************\n")
running = True

while running == True:
    print('1. Add two numbers')
    print('2. Print your name')
    print('3. Quit')

    user_input = int(input('Enter an option'))

    if user_input == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        answer = num1 + num2
        print(num1, '+', num2, " = ", answer)

    if user_input == 2:
        name = input("Enter your name: ")
        print("hello,", name)

    if user_input == 3:
        running = False

print('goodbye')
