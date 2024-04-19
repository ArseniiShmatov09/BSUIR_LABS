def is_corner_vertex(B, i, j):
    """
    Проверяет, является ли вершина угловой.
    """
    # Получаем индексы соседних вершин
    neighbors = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    for k in range(4):
        # Индексы вершин
        v1 = B.index((i, j))
        v2 = B.index(neighbors[k % 4])
        v3 = B.index(neighbors[(k + 1) % 4])
        v4 = B.index(neighbors[(k + 2) % 4])
        # Векторы ребер
        vec1 = (B[v2][0] - B[v1][0], B[v2][1] - B[v1][1])
        vec2 = (B[v4][0] - B[v3][0], B[v4][1] - B[v3][1])
        # Проверяем перпендикулярность
        if vec1[0] * vec2[0] + vec1[1] * vec2[1] == 0:
            return True
    return False

def find_corner_vertices(B):
    """
    Находит угловые вершины в графе, основываясь на списке индексов B.
    """
    corner_vertices = []
    for i, j in B:
        if is_corner_vertex(B, i, j):
            corner_vertices.append((i, j))
    return corner_vertices

# Пример данных
B = [[1, 1], [2, 1], [2, 2], [3, 2], [3, 3]]

# Преобразуем координаты B в кортежи
B = [(i-1, j-1) for i, j in B]

# Находим угловые вершины
corner_vertices = find_corner_vertices(B)

# Выводим результат
print("Угловые вершины:")
print(corner_vertices)
