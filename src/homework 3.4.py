#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
#Входные данные - строка из чисел, разделенная пробелами.
#Выходные данные - количество пар.

st = input().split()
couple = 0
for i in range(len(st)):
    for j in range(i+1, len(st)):
        if st[i] == st[j]:
            couple += 1
print(couple)

