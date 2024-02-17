"""
Напишите функцию для транспонирования матрицы
"""


def trans_matrix(matrix: tuple) -> list:
    new_list = []
    for i in range(len(matrix[0])):
        new_list.append([])
        for j in range(len(matrix)):
            new_list[i].append(matrix[j][i])
    return new_list


my_matrix = ((2, 4),
             (1, 6),
             (3, 8)
             )
for row in trans_matrix(my_matrix):
    print(*row)
