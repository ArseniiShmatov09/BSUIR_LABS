import numpy as np
from utils import matrix_inverse

itr = 1
def main_simplex_method(m, n, A, b, c_T, x_T, j, A_B, A_B_inv, tmp_x_T, tmp_j):
    global itr

    print("Итерация №", itr)
    c_B_T = [c_T[col_idx - 1] for col_idx in j[1:]]
    
    print("Вектор c_B_T:")
    print(c_B_T)

    u_T = np.dot(c_B_T, A_B_inv)
    print("Вектор потенциалов u_T:")
    print(u_T)

    delta_T = np.dot(u_T, A) - c_T
    print("Вектор оценок delta_T:")
    print(delta_T)

    for i in range(delta_T.shape[0]):
        if delta_T[i] < 0:
            j[0] = i + 1 
            break
    
    print("j[0]: ")
    print(j[0]) 

    if(j[0] == -1):
        print("Оптимальный план: " )
        return x_T, j
            

    else:
        z = np.dot(A_B_inv, A[:, j[0] - 1])
        print("Вектор z:")
        print(z)    

        theta_T = []
        for i in range(0, m):
            if z[i] <= 0:
                theta_T.append(np.Infinity)
            else:
                theta_T.append(x_T[j[i + 1] - 1]/z[i])
        print("Вектор theta_T:")
        print(theta_T)

        theta_T_0 = min(theta_T)
        
        if(theta_T_0 == np.Infinity):
            return ("Целевой функционал задачи (1) не ограничен сверху на множестве допустимых планов")
        else:

            k = theta_T.index(theta_T_0) + 1
            j_star = j[k]
            j[k] = j[0]

            x_T[j[0] - 1] = theta_T_0
            for i in range(1, m):
                if(i!=k):
                    x_T[j[i] - 1] = x_T[j[i] - 1] - theta_T_0 * z[i - 1]
            x_T[j_star - 1] = 0
            j[0] = -1

            print("Новый x_T:")
            print(x_T)
            print("Новый j:")
            print(j)


            x = A[:, j[k] -1]
            X = []
            for el in x:
                X.append([el])
            XX = np.array(X)

            new_A_B_inv = matrix_inverse(m, A_B, A_B_inv, XX, k - 1)
            print (new_A_B_inv[0])
            print (new_A_B_inv[1])
            
            if tmp_x_T == x_T:
                print("Оптимальный план: " )
                return x_T, j
            
            tmp_x_T = x_T
            tmp_j = j

            itr+=1
            return main_simplex_method(m, n, A, b, c_T, x_T, j, new_A_B_inv[0], new_A_B_inv[1], tmp_x_T, tmp_j)

def main():

    m = int(input("Введите количество строк в матрице A: "))
    n = int(input("Введите количество столбцов в матрице A: "))
   
    print("Введите значения матрицы A:")
    matrix = []
    for _ in range(m):
        row = list(map(float, input().split()))
        matrix.append(row)

    print("Введите значения вектора-столбца b:")
    b = []
    for _ in range(m):
        element = float(input())
        b.append(element)
   
    print("Введите значения вектора коэффициентов при переменных c_T:")
    c_T = list(map(float, input().split()))

    A = np.array(matrix)
    print("Введите первый компонент начального базисного допустимого плана x_T: ")
    x_T = list(map(float, input().split()))
    
    print("Введите второй компонент начального базисного допустимого плана B: ")
    jj = list(map(int, input().split()))

    j = []
    j.append(-1)
    for i in range(m):
        j.append(jj[i])
    

    A_B = A[:, [col_idx - 1 for col_idx in j if col_idx != -1]]

    A_B_inv = np.linalg.inv(A_B)

    print("Матрица A:")
    print(A)
    print("Вектор b:")
    print(b)
    print("Вектор c_T:")
    print(c_T)
    print("Матрица A_B:")
    print(A_B)
    print("Матрица A_B_inv:")
    print(A_B_inv)


    tmp_x_T = []
    tmp_j = []
    
    print(main_simplex_method(m, n, A, b, c_T, x_T, j, A_B, A_B_inv, tmp_x_T, tmp_j)[0])    


if __name__ == "__main__":

    main()

