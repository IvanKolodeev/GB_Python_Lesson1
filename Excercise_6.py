# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = input("Enter a six-digit ticket number: ")

if len(number) != 6 or not number.isdigit():
    print("Invalid input. Please enter a six-digit number.")
else:
    number = int(number)
    digit1 = number // 100000
    digit2 = (number // 10000) % 10
    digit3 = (number // 1000) % 10
    digit4 = (number // 100) % 10
    digit5 = (number // 10) % 10
    digit6 = number % 10
    sum1 = digit1 + digit2 + digit3
    sum2 = digit4 + digit5 + digit6

    if sum1 == sum2:
        print("lucky ticket")
    else:
        print("no luck today")