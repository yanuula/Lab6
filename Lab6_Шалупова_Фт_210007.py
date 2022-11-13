import numpy as np
while True:
    try:
        cr_amount = int(input("Введите количество критериев: "))
        break
    except ValueError:
        print('Количество критериев должно быть положительным целым числом')
#Матрица
matr = np.eye(cr_amount)
#Заполнение матрицы коэффициентами
a = 1
for p in range(a, cr_amount+1):
    for q in range(a+1, cr_amount+1):
        while True:
            try:
                #Заполнение каждого элемента строки матрицы
                matr[p-1][q-1] = round(float(input('Введите отношение критериев {0}-{1}: '.format(p, q))), 3)
                break
            except ValueError:
                print('Неверный ввод')
        #Заполнение ячеек для обратного соотношения
        matr[q-1][p-1] = round(matr[p-1][q-1]**(-1), 2)
    a += 1
#Суммы строк
sum_matr = [round(sum(j),2) for j in matr]
sum_matr1 = [round(n/sum(sum_matr), 2) for n in sum_matr]
if (sum(sum_matr1)) != 1.0:
    index = sum_matr1.index(max(sum_matr1))
    k = (sum(sum_matr1)) - 1.0
    sum_matr1[index] -= k
print('Весовые коэффициенты: ')
for ind in sum_matr1:
    print(ind, end=' ')
