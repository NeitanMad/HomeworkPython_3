# ������ 22
def find_common_elements(set1, set2):
    common_elements = sorted(list(set(set1) & set(set2)))
    return common_elements

n = int(input("������� ���������� ��������� ������� ���������: "))
m = int(input("������� ���������� ��������� ������� ���������: "))

set1 = set()
set2 = set()

for _ in range(n):
    element = int(input('������� ������� ������� ���������: '))
    set1.add(element)

for _ in range(m):
    element = int(input('������� ������� ������� ���������: '))
    set2.add(element)

result = find_common_elements(set1, set2)
print('����� ������� ����������� � ����� ����������: ')
print(result)

# ������ 24
n_bushes = int(input('������� ���������� ������ �������: '))
arr = list()

for i in range(n_bushes):
    a =int(input('������� ���������� ���� �� �����: '))
    arr.append(a)

arr_count = list()

for i in range(len(arr)):
       arr_count.append(arr[i-2] + arr[i-1] + arr[i])

print(max(arr_count))