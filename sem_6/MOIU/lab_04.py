import numpy as np

itr = 1
def dual_simplex_method(m, n, A, b, c_T, B):
    global itr
    print("Итерация №", itr)

    #STEP 1
    A_B = A[:, [col_idx - 1 for col_idx in B if col_idx != -1]]
    print('A_B: ')
    print(A_B)

    A_B_inv = np.linalg.inv(A_B)
    print('A_B_inv: ')
    print(A_B_inv)

    #STEP 2
    c_B_T = [c_T[col_idx - 1] for col_idx in B]
    print("Вектор c_B_T:")
    print(c_B_T)

    #STEP 3
    y_T = np.dot(c_B_T, A_B_inv)
    print('y_T: ')
    print(y_T)

    #STEP 4
    k_B = list(np.dot(A_B_inv, b))
    k_T = [0 if i not in B else k_B[B.index(i)] for i in range(1, n + 1)]

    print('k_T:')
    print(k_T)

    #STEP 5
    is_optimal = True
    for i in range (len(k_T)):
        if k_T[i] < 0 and k_T[i] != -1:
           #STEP 6
            j_k = i + 1
            print('j_k:')
            print(j_k)
            is_optimal = False
            break
    
    if(is_optimal):
        print("Оптимальный план: ")
        return k_T

    for i in range(len(B)):
        if B[i] == j_k:
            k = i + 1
    
    print('k:')
    print(k)
    
    #STEP 7
    delta_y_T = A_B_inv[k - 1, :]
    print('delta_y_T:')
    print(delta_y_T)
  
    mu = [-1] * (n)

    is_compatible = False
    for i in range(1, n + 1):
        if i not in B:
            mu[i - 1] = np.dot(delta_y_T, A[:, i - 1])
            if(mu[i - 1] < 0):
                is_compatible = True
    print('mu')
    print(mu)

    #STEP 8
    if(not is_compatible):
        return('Прямая задача (1) не совместна')

    #STEP 9
    sigma = [-1] * (n)
    sigma_0 = 9999999999999999
    for i in range(1, n + 1):
        if i not in B and mu[i - 1]< 0:
            sigma[i - 1] = (c_T[i - 1] - (np.dot(np.transpose(A[:, i - 1]), np.transpose(y_T)))) / mu[i - 1]
            
            #STEP 10
            if sigma[i - 1] < sigma_0:
                sigma_0 = sigma[i - 1]
                j_0 = i


    print('sigma:')
    print(sigma)
    print('sigma_0:')
    print(sigma_0) 
    print('j_0:')
    print(j_0)
    
    #STEP 11
    B[k - 1] = j_0
    print('Новое множество базисных индексов B:')

    print(B)

    itr += 1
    return(dual_simplex_method(m, n, A, b, c_T, B))


def main():

    m = int(input("Введите количество строк в матрице A: "))
    n = int(input("Введите количество столбцов в матрице A: "))
   
    print("Введите значения матрицы A:")
    matrix = []
    for _ in range(m):
        row = list(map(float, input().split()))
        matrix.append(row)

    A = np.array(matrix)

    print("Введите значения вектора-столбца b:")
    b = []
    for _ in range(m):
        element = float(input())
        b.append(element)
    
    print("Введите значения вектора коэффициентов при переменных c_T:")
    c_T = list(map(float, input().split()))

    print("Введите значения множества B:")
    B = list(map(int, input().split()))

    print("Матрица A:")
    print(A)
    print("Вектор b:")
    print(b)
    print("Вектор c_T:")
    print(c_T)
    print("Множество B:")
    print(B)

    result = dual_simplex_method(m, n, A, b, c_T, B)
    print(result)


if __name__ == "__main__":
    main()