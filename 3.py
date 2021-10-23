def function(a):
    b = str(abs(a))
    if a < 0 :
        c = "-"
    else :
        c = ""
    for i in range (len(b) - 1, -1, -1):
        c = c + b[i]
    return (int(c))

a = int(input('Input: '))
print(f'Output: {function(a)}')
