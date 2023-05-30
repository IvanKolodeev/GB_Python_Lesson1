# Задача 2: Найдите сумму цифр трехзначного числа.

number = input("Enter a three-digit number: ")

if len(number) != 3 or not number.isdigit():
    print("Invalid input. Please enter a three-digit number.")
else:
    number = int(number)
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    digit_sum = digit1 + digit2 + digit3
    print("The sum of the digits is:", digit_sum)