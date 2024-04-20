import numpy as np
from collections import Counter
from copy import deepcopy

tests = {
    "1": [3, [100, 300, 300], 3, [300, 200, 200], [[8, 4, 1],
                                                   [8, 4, 3],
                                                   [9, 7, 5]]],
    "2": [4, [21, 19, 15, 25], 5, [15, 15, 15, 15, 20], [[30, 24, 11, 12, 25],
                                                         [26, 4, 29, 20, 24],
                                                         [27, 14, 14, 10, 18],
                                                         [6, 14, 28, 8, 2]]],
    "3": [2, [15, 5], 3, [6, 9, 5], [[20, 30, 40],
                                     [30, 70, 70]]]



}

def balance(data:list):
    m = data[0]
    a = data[1]
    n = data[2]
    b = data[3]
    C = data[4]

    if sum(a) > sum(b):
        b.append(sum(a) - sum(b))
        n+=1
        C = np.append(C, [[0] * C.shape[0]], axis=1)
    elif sum(a) < sum(b):
        a.append(sum(b) - sum(a))
        m += 1
        C = np.append(C, [[0] * C.shape[1]], axis=0)
  
    return a, b, m, n, C

def first_basis_plan(data: list):
    
    balanced_data = balance(data)
   
    a = balanced_data[0]
    b = balanced_data[1]
    m = balanced_data[2]
    n = balanced_data[3]
    C = balanced_data[4]

    B = []
    B.append((1, 1))

    i = 0
    j = 0
    X = np.zeros((m, n))

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
            B.append((i + 1, j + 1))

    print("Нчальный базисный план: ")
    print('\n', X)
    print('\n', B)
    new_res = [m, a, n, b, C, X, B]
    return new_res

def create_variables_list(prefix, count):
    return [f"{prefix}{i+1}" for i in range(count)]

itr = 1

def potential_method_second_phase(plan:list):
    m = plan[0]
    a = plan[1]
    n = plan[2]
    b = plan[3]
    C = plan[4]
    X = plan[5]
    B = plan[6]

    global itr
    print("Итерация №", itr, '\n')

    u = create_variables_list('u', m)
    v = create_variables_list('v', n)
    
    M1 = np.zeros((len(B),n + m), dtype=int)

    for idx, (i, j) in enumerate(B):
        M1[idx, u.index(f"u{i}")] = 1
        M1[idx, len(u) + v.index(f"v{j}")] = 1

    M1 = np.insert(M1, 0, np.concatenate(([1], np.zeros(n + m - 1))), axis=0)
    v1 = np.array([C[i - 1][j - 1] for i, j in B])
    v1 = np.insert(v1, 0, 0)
    solved_uv = np.linalg.solve(M1, v1)
    solved_u = solved_uv[:m] 
    solved_v = solved_uv[m:] 

    print("Значения для переменных u:", solved_u, '\n')
    print("Значения для переменных v:", solved_v, '\n')

    is_optimal = True
    for i in range(m):
        for j in range(n):
            if solved_u[i] + solved_v[j] > C[i][j]:
                is_optimal = False
                i_ = i + 1
                j_ = j + 1
                break
        if not is_optimal:
            break    
        
    if(is_optimal):
       print("Оптимальный план: ", '\n')
       return X
    else:
        B.append((i_, j_))

    B_copy = deepcopy(B)
    
    while True:
        i_list = [i for (i, j) in B_copy]
        j_list = [j for (i, j) in B_copy]

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
            for index, (i, j) in enumerate(B_copy):
                if plus[-1][0] == i or plus[-1][1] == j:
                    minus.append(B_copy.pop(index))
                    break
        else:
            for index, (i, j) in enumerate(B_copy):
                if minus[-1][0] == i or minus[-1][1] == j:
                    plus.append(B_copy.pop(index))
                    break
    
    print("Угловые вершины +:")
    print(plus, '\n')
    print("Угловые вершины -")
    print(minus, '\n')
    
    theta = min(X[i - 1][j - 1] for i, j in minus)
    print("Тета: ")
    print(theta, '\n')

    for i, j in plus:
        X[i - 1][j - 1] += theta
    for i, j in minus:
        X[i - 1][j - 1] -= theta

    for i, j in minus:
        if X[i - 1][j - 1] == 0:
            B.remove((i, j))
            break
    itr += 1

    print("Новое множество базисных позиций: ")
    print(B)

    plan = [m, a, n, b, C, X, B]
    return potential_method_second_phase(plan)

def main():

    plan = first_basis_plan(tests['1'])
    res = potential_method_second_phase(plan)

    print(res)


if __name__ == "__main__":
    main()