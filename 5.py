def function(a):
    for i in range (2, a):
        if (a % i == 0):
            return "false"
    return "true"

a = int(input("Введите число: "))
print(function(a))
