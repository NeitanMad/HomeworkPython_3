def find_common_elements(set1, set2):
    common_elements = sorted(list(set(set1) & set(set2)))
    return common_elements

n = int(input("������� ���������� ��������� ������� ���������: "))
m = int(input("������� ���������� ��������� ������� ���������: "))

set1 = set()
set2 = set()

for _ in range(n):
    element = int(input("������� ������� ������� ���������: "))
    set1.add(element)

for _ in range(m):
    element = int(input("������� ������� ������� ���������: "))
    set2.add(element)

result = find_common_elements(set1, set2)
print("�����, ������� ����������� � ����� ������� ��� ���������� � ������� �����������:")
print(result)
