# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что
# Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

total = input("How many cranes were made?")
if total.isdigit():
    total = int(total)
    kate = total * 2/3
    peter = total * 1/3 / 2
    print("Kate made", kate, "cranes")
    print("Peter made", peter, "cranes")
    print("Sergey made", peter, "cranes")

else:
    print("Invalid input. Please enter a three-digit number.")






