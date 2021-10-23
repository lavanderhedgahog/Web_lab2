def function(list):
    listTwo = []
    listThree = []
    listFive = []
    for i in range (len(list)):
        if list[i]%2 == 0:
            listTwo.append(list[i])
        if list[i]%3 == 0:
            listThree.append(list[i])
        if list[i]%5 == 0:
            listFive.append(list[i])
    return (listTwo, listThree, listFive)

n = int(input("Введите количество чисел: "))
list = []
print("Введите числа через enter")
for i in range (0,n,1):
    list.append(int(input()))

print(function(list))
