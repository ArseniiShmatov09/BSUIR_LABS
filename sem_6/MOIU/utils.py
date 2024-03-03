import numpy as np

def matrix_inverse(n, A, A_inv, X, i):
    A_prime = np.copy(A)
    A_prime[:, i] = X[:, 0]

    l = np.dot(A_inv, X)
    if l[i] == 0:
        return("Матрица A_prime необратима")

    else: 
        l_tilde = np.copy(l)
        l_tilde[i] = -1

        l_hat = -1 / l[i] * l_tilde

        Q = np.eye(n)
        Q[:, i] = l_hat[:, 0]

        A_prime_inv = [0] * n 
        for i in range(n): 
            A_prime_inv[i] = [0] * n 

        for j in range(n):
            for k in range(n):
                if i != j:
                    A_prime_inv[j][k] = Q[j][j] * A_inv[j][k] + Q[j][i] * A_inv[i][k]
                else:
                    A_prime_inv[j][k] = Q[j][i] * A_inv[i][k]


        return([A_prime, A_prime_inv])
