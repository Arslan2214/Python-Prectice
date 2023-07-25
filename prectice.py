# ---- Age Identifier Projects ----






# 1. Age Checker
# age = int(input('Enter Age: '))
# if age > 18 :
#     print('You are Not a Kid.')
# else:
#     print("You are a Kid.")

#  --------------------------------

# 2. Number Gussing Game

# import sys
# import random
# def numGuess():
#     num = random.randint(0, 25)
#     chance = 8
#     while (chance != 0):
#         inp = int(input('Enter Number: '))
#         if inp == num:
#             return print(f'Correct, You win.... {num} is Right')
#         else:
#             if inp < num:
#                 print('You Enter low number ')
#             else:
#                 print('You Enter High number ')

#             chance -= 1
#             print(f'You have {chance} left.')

# numGuess()

# -------------------------------

# 3. Basic Calculator using Python

# def calculator():
#     num1 = int(input('Enter 1st Num: '))
#     num2 = int(input('Enter 2nd Num: '))
#     oper = str(input('Enter Opereration: '))

#     if oper == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif oper == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     elif oper == '*':
#         print(f'{num1} * {num2} = {num1 * num2}')
#     elif oper == '/':
#         print(f'{num1} / {num2} = {num1 / num2}')
#     else:
#         print(f'"{oper}" is Not Valid.')

# calculator()

# ----------------------------------

# 4. Rolling Dice

# import random

# def dice():
#     dice = int(input('Number of Dices:'))
#     for i in range(dice):
#         side = int(input('Enter Sides:'))
#         print(f'{i+1}\'s Dice: {random.randint(1, side)}')

# dice()

# -----------------------------------


# 5. Generate Code Function
import random
import string

def generate_code(length):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return code

# Generate a 6-character code
num = int(input('Enter Code-Length:'))
generated_code = generate_code(6)
print(generated_code)

# -------------------------------

# 6. Basic Calculator
num1 = int(input('Num1:'))
num2 = int(input('Num2:'))
op = input('Op:')
if (op == '+')
{
    print(f"{num1} + {num2}: {num1 + num2}")
}
elif (op == '-')
{
    print(f"{num1} - {num2}: {num1 - num2}")
}
elif (op == '*' or op == 'x' or op == 'X' )
{
    print(f"{num1} x {num2}: {num1 * num2}")
}
elif (op == '/')
{
    print(f"{num1} / {num2}: {num1 / num2}")
}
else
{
    print('This Operation is Not Supported. (Try Else)')
}
