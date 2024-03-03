import numpy as np

from lab_02 import main_simplex_method 

def simplex_method_begin_stage(m, n, A, b):

    for i in range(len(b)):
        if b[i] < 0:
            b[i]*= -1
            for j in range(n):
                A[i][j] *= -1

    c_T_tilda = []

    for i in range(0, n):
        c_T_tilda.append(0)
    
    for i in range(0, m):
        c_T_tilda.append(-1)

    E = np.eye(m)
    A_tilda = np.concatenate((A, E), axis=1)

    x_T_tilda = []

    for i in range(0, n):
        x_T_tilda.append(0)

    for i in range(0, m):
        x_T_tilda.append(b[i])

    B = []

    for i in range(0, m + 1):
        B.append(n + i)
    
    B[0] = -1 

    A_B = A_tilda[:, [col_idx - 1 for col_idx in B if col_idx != -1]]

    A_B_inv = np.linalg.inv(A_B)

    new_optimal_plan = main_simplex_method(m, n, A_tilda, b, c_T_tilda, x_T_tilda, B, A_B, A_B_inv, [], [])
    
    x_T_tilda = new_optimal_plan[0]
    B = new_optimal_plan[1]

    A_B = A_tilda[:, [col_idx - 1 for col_idx in B if col_idx != -1]]

    A_B_inv = np.linalg.inv(A_B)

    for i in range(0, m):
        if x_T_tilda[n + i] != 0:
            return ("Задача не совместна")

    x_T = []

    for i in range(0, n):
        x_T.append(x_T_tilda[i])
                    
    return recurse_steps(n, A, b, x_T, B, A_B_inv, A_tilda)
   


def recurse_steps(n, A, b, x_T, B, A_B_inv, A_tilda):
     #STEP 7
    if all(element <= n for element in B):
        return x_T, B, A, b
    
    else:
        k = len(B) - 1

        j = []
        for i in range(n):
            j.append(i + 1)
        
        j = list(set(j) - set(B))

        l = [-1] * (n + 1)
        a = True
        for i in j:
            matrix = np.dot(A_B_inv, A_tilda[:, i - 1])
            l[i] = matrix
            
            if l[i][k - 1] != 0:
                j[k] = i
                a = False
        
        if(a):
           A = np.delete(A, k - 1, axis=0) 
           b.pop(k - 1)
           B.pop(k)
           A_tilda = np.delete(A_tilda, k - 1, axis=0) 
        return recurse_steps(n, A, b, x_T, B, A_B_inv, A_tilda)

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

    print("Матрица A:")
    print(A)
    print("Вектор b:")
    print(b)
    print("Вектор c_T:")
    print(c_T)


    result = simplex_method_begin_stage(m, n, A, b)
    print("x_T:")
    print(result[0])
    print("B:")
    print(result[1])
    print("A:")
    print(result[2])
    print("b:")
    print(result[3])


if __name__ == "__main__":
    main()