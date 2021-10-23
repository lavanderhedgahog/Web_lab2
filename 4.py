def function(a,n):
    a0 = 1
    b = (1 / n) * ((n - 1) * a0 + (a / (a0 ** (n - 1))))
    while (abs(b - a0) > 0.1):
        a0 = b
        b = (1 / n) * ((n - 1) * a0 + (a / (a0 ** (n - 1))))
    return b
    
n = int(input("Введите степень корня: "))
a = int(input("Введите число: "))
print(function(a,n))
