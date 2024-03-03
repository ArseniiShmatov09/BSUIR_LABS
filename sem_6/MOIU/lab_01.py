import numpy as np

def main():
    n = int(input("Введите порядок квадратной матрицы: "))

    print("Введите значения матрицы А:")
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    print("Введите значения обратной матрицы А:")
    matrix_inv = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix_inv.append(row)

    print("Введите значения вектора-столбца x:")
    x = []
    for _ in range(n):
        element = float(input())
        x.append([element])

    i = int(input("Введите номер столбца (от 1 до {}): ".format(n))) - 1

    A = np.array(matrix)
    A_inv = np.array(matrix_inv)

    X = np.array(x)

    A_prime = np.copy(A)
    A_prime[:, i] = X[:, 0]

    print("Исходная матрица A:")
    print(A)
    print("Обратная матрица A_inv:")
    print(A_inv)
    print("Вектор x:")
    print(X)
    print("Матрица A_prime (i-ый столбец заменен на вектор-столбец x):")
    print(A_prime)

    #STEP 1
    l = np.dot(A_inv, X)

    print("Вектор l: ")
    print(l)

    if l[i] == 0:
        print("Матрица A_prime необратима")
    
    #STEP 2
    else: 
        l_tilde = np.copy(l)
        l_tilde[i] = -1
        print("Вектор l_tilde:")
        print(l_tilde)

        #STEP 3
        l_hat = -1 / l[i] * l_tilde
        print("Вектор l_hat:")
        print(l_hat)

        #STEP 4
        Q = np.eye(n)
        Q[:, i] = l_hat[:, 0]

        print("Матрица Q:")
        print(Q)

        #STEP 5
        A_prime_inv = [0] * n 
        for i in range(n): 
            A_prime_inv[i] = [0] * n 

        for j in range(n):
            for k in range(n):
                if i != j:
                    A_prime_inv[j][k] = Q[j][j] * A_inv[j][k] + Q[j][i] * A_inv[i][k]
                else:
                    A_prime_inv[j][k] = Q[j][i] * A_inv[i][k]
        
        print("Матрица A_prime_inv:")
        print(A_prime_inv)
        
if __name__ == "__main__":
    main()
