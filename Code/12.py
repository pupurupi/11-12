# Вариант 12. Создайте функцию для генерации всех сочетаний размера k из n элементов. 
def combinations(n, k, start, current, result):
    #База индукции (если остался только один набор, то его копию добовляем в результат)
    if len(current)==k:
        result.append(current[:])
        return result
    #Рекурсивная часть (берём  первое число, и проходим по порядку, добирая оставшиеся наборы)
    for i in range(start, n+1):
        current.append(i)
        combinations(n, k, i+1, current, result)
        current.pop() #Backtrack
current=[]
result=[]
combinations(5, 3, 1, current, result)
print('Все сочетания С({n}, {k}):')
for i in result:
    print(i)