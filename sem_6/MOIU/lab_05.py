import numpy as np
from collections import Counter
from copy import deepcopy

def potential_method_first_phase(m:int, a:list, n:int, b:list):
    
    if sum(a) > sum(b):
        b.append(sum(a) - sum(b))
        n+=1
        #C[i n+1] = 0
    elif sum(a) < sum(b):
        a.append(sum(b) - sum(a))
        m+=1
        #C[m+1 j] = 0

    X = np.zeros((m, n))
    B = []
    B.append([1, 1])

    i = 0
    j = 0
    while(i!= m and j!= n):
        if a[i] <= b[j]:
                X[i][j] += a[i]
                b[j] -= a[i] 
                a[i] = 0
                i+=1
        elif a[i] > b[j]:
                X[i][j] += b[j]
                a[i] -= b[j] 
                b[j] = 0
                j+=1
        if(i!= m and j!= n):
            B.append([i + 1, j + 1])

    print('\n', X)
    print('\n', B)
    return X, B, m, n

def create_variables_list(prefix, count):
    return [f"{prefix}{i+1}" for i in range(count)]

def potential_method_second_phase(m:int, a:list, n:int, b:list, C:list):
    beginning_res = potential_method_first_phase(3, [100, 300, 300], 3, [300, 200, 200])
    X = beginning_res[0]
    B = beginning_res[1]
    m = beginning_res[2]
    m = beginning_res[3]
    u = create_variables_list('u', m)
    v = create_variables_list('v', n)
    print(u)
    print(v)
    
    M1 = np.zeros((len(B),n + m), dtype=int)

    for idx, (i, j) in enumerate(B):
        M1[idx, u.index(f"u{i}")] = 1
        M1[idx, len(u) + v.index(f"v{j}")] = 1

    M1 = np.insert(M1, 0, np.concatenate(([1], np.zeros(n + m - 1))), axis=0)
    print(M1)
    v1 = np.array([C[i - 1][j - 1] for i, j in B])
    v1 = np.insert(v1, 0, 0)
    print(v1)
    solved_uv = np.linalg.solve(M1, v1)
    solved_u = solved_uv[:m] 
    solved_v = solved_uv[m:] 

    print("Значения для переменных u:", solved_u)
    print("Значения для переменных v:", solved_v)

    i_ = 0
    j_ = 0
    is_optimal = True
    for i in range(m):
        for j in range(n):
            if solved_u[i] + solved_v[j] <= C[i][j]:
                is_optimal = False
                i_ = i + 1
                j_ = j + 1

    if(is_optimal):
       return X
    else:
        B.append[i_, j_]

    B_copy = deepcopy(B)
    
    while True:
        i_list = [i for [i, j] in B_copy]
        j_list = [j for [i, j] in B_copy]

        i_counter = Counter(i_list)
        j_counter = Counter(j_list)

        i_to_rm = [i for i in i_counter if i_counter[i] == 1]
        j_to_rm = [j for j in j_counter if j_counter[j] == 1]

        if not i_to_rm and not j_to_rm:
            break
        B_copy = [(i, j) for (i, j) in B_copy if i not in i_to_rm
                    and j not in j_to_rm]  

    plus, minus = [], []
    plus.append(B_copy.pop())

    while B_copy:
        if len(plus) > len(minus):
            for index, [i, j] in enumerate(B_copy):
                if plus[-1][0] == i or plus[-1][1] == j:
                    minus.append(B_copy.pop(index))
                    break
        else:
            for index, [i, j] in enumerate(B_copy):
                if minus[-1][0] == i or minus[-1][1] == j:
                    plus.append(B_copy.pop(index))
                    break
    
    theta = min(X[i][j] for i, j in minus)
   
    for i, j in plus:
        X[i][j] += theta
    for i, j in minus:
        X[i][j] -= theta

    for i, j in minus:
        if X[i][j] == 0:
            B.remove((i, j))
            break
    
    return potential_method_second_phase(m, a, n, b, C)

def main():
    # m = int(input("Введите количество пунктов отправления: "))
    # a = list(map(float, input("Введите количество ед. продукции в каждли пункте отпрааления").split()))
    
    # n = int(input("Введите количество пунктов назначения: "))
    # b = list(map(float, input("Введите количество ед. продукции в каждли пункте назначения").split()))

    potential_method_second_phase(3, [100, 300, 300], 3, [300, 200, 200], [[8, 4, 1],
                                                                           [8, 4, 3],
                                                                           [9, 7, 5]])




if __name__ == "__main__":
    main()