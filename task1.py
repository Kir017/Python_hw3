import random
number = int(input('Введите длину массива:' ))
desiredNumber = int(input('Введите искомое число:' ))
count = 0
list = []
for i in range(1,number+1):
    i = random.randint(1,number)
    list.append(i)
print(list)
for j in range(len(list)):
    if desiredNumber == list[j]:
        count += 1
print(f'Число {desiredNumber} в массиве встречается {count} раз(а)')