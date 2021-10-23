def function(a):
    a = abs(a);
    while len(str(a)) > 1:
        b = a//(10**(len(str(a))-1))
        c = a%10
        if b != c:
            return ("false")
        a = (a%(10**(len(str(a))-1)))//10
    return ("true")

a = int(input("Enter number: "))

print(f"Polinom? {function(a)}")
