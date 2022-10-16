import sys
import msvcrt as m
def convertToInt(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n
#матрица
def inputTable(table, n):
    for i in range(n):
        for j in range(n):
            if (i == j):
                table[i][j] = 1
            if (i < j):
                while table[i][j] == 0:
                    temp = input("Введите отношение критерия {0} к критерию {1}: ".format(i+1, j+1))
                    temp = convertToInt(temp)
                    if (temp == -1) or (1 <= temp <= 9) == False: 
                        print('Отношение должно быть целым числом от 1 до 9')
                    else:
                        table[i][j] = temp
    for i in range(n):
        for j in range(n):
            if (i > j):
                table[i][j] = 1/table[j][i]
    return table
def tableSum(table, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += table[i][j]
    return sum
def countWQ(table,n,sum):
    columnSum = 0
    arrayWQ  = list()
    for i in range(n):
        for j in range(n):
            columnSum += table[j][i]
        arrayWQ.append(columnSum/sum)
    return arrayWQ
n = 0
#Ввод количества критериев
while n == 0:
    n = input("Введите количество критериев: ")
    n = convertToInt(n)
    if (n == -1) or (n < 1):
        print("Количество критериев должно быть положительным целым числом")
        n = 0
a = [[0] * n for i in range(n)]
a = inputTable(a,n)
a_sum = tableSum(a,n)
WQ = countWQ(a,n,a_sum)
WQ.reverse()
print("Весовые коэффициенты:", end=" ") #Вывод весовых коэффицентов
for elem in WQ:
    print("{0:.2f}".format(elem), end=" ")
m.getch()
sys.exit()
