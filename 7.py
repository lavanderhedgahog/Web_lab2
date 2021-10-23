cashe = []
counter = []
n = 0

def decorator(function):
    def wrapper(food):
        if len(cashe) != 0 :
            if counter[0] == 0 :
                cashe.pop(0)
                counter.pop(0)
            print (cashe)
            for i in range (len(cashe)):
                counter[i] -= 1
        cashe.append(function(food))
        counter.append(n)
    return wrapper
@decorator

def sandwich(food):
    return food

n = int(input())

sandwich("ветчина")
sandwich("помидор")
sandwich("огурчик")
sandwich("хлебушек")
sandwich("салат")
sandwich("горошек")
sandwich("стив")
sandwich("яблочко")
sandwich("ручка")
