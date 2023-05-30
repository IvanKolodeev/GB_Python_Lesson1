# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить ровно k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

def can_break_chocolate(n, m, k):
    if k % n == 0 or k % m == 0:
        return True
    if k < n and n % k == 0:
        return True
    if k < m and m % k == 0:
        return True
    return False

n = input("Please enter chocolate bar length: ")
m = input("Please enter chocolate bar width: ")
k = input("How many pieces do you want: ")

if n.isdigit() and m.isdigit() and k.isdigit():
    n = int(n)
    m = int(m)
    k = int(k)
    if can_break_chocolate(n, m, k):
        print("It is possible to break off", k, "slices.")
    else:
        print("It is not possible to break off", k, "slices.")

else:
    print("Invalid input. Please enter numbers only")