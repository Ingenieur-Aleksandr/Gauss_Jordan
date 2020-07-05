# метод Гаусса-Жордана
import numpy as np
def gauss_jordan(m, eps = 1.0/(10**10)):
    #Преобразует матрицу на входе по методу Гаусса-Жордана
    #True = успешно, False = сингулярное решение
    (h, w) = (len(m), len(m[0]))
    for i in range(0, h):
        maxrow = i
        for j in range(i+1, h):    # Поиск строки с максимальным первым значением
            if abs(m[j][i]) > abs(m[maxrow][i]):
                maxrow = j
        (m[i], m[maxrow]) = (m[maxrow], m[i])    # Постановка строки с макс. знач. на первую позицию
        if abs(m[i][i]) <= eps:     # Проверка на наличие нулей на главной диагонали
            return False
        for j in range(i+1, h):    # Прямой ход, зануление снизу
            c = m[j][i] / m[i][i]
            for k in range(i, w):
                m[j][k] -= m[i][k] * c
    for i in range(h-1, 0-1, -1): # Обратный ход, зануление сверху
        c  = m[i][i]
        for j in range(0,i):
            for k in range(w-1, i-1, -1):
                m[j][k] -=  m[i][k] * m[j][i] / c
        m[i][i] /= c
        for k in range(h, w):       # Приведение к единице
            m[i][k] /= c
    return True
mtx = [[1.0, 1.0, 1.0, 0.0],
       [4.0, 2.0, 1.0, 1.0],
       [9.0, 3.0, 1.0, 3.0]]
print(np.array(mtx))

if gauss_jordan(mtx) == True:
    print(np.array(mtx))
else:
    print("Singular!")
# для сравнения пример алгоритма из numpy
mtx2 = np.mat("1.0, 1.0, 1.0; 4.0, 2.0, 1.0; 9.0, 3.0, 1.0")
print(mtx2)
b = np.array([0, 1, 3])
print(b)
z = np.linalg.solve(mtx2, b)
print(z)