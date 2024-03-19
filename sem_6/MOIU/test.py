k_B = [-1, -1.5]  # список k_B
B = [4, 5]        # список B

# Создаем список k_T, заполненный нулями
k_T = [0 if i not in B else k_B[B.index(i)] for i in range(1, 6)]

print(k_T)
