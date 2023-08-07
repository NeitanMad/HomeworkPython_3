def find_common_elements(set1, set2):
    common_elements = sorted(list(set(set1) & set(set2)))
    return common_elements

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

for _ in range(n):
    element = int(input("Введите элемент первого множества: "))
    set1.add(element)

for _ in range(m):
    element = int(input("Введите элемент второго множества: "))
    set2.add(element)

result = find_common_elements(set1, set2)
print("Числа, которые встречаются в обоих наборах без повторений в порядке возрастания:")
print(result)
