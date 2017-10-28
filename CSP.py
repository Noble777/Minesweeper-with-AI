import numpy as N

def matrix_expand(row_0, column_0, mat_0):
    mat_1 = N.zeros((row_0 + 2, column_0 + 2), dtype=int)
    for i in range(0, row_0):
        for j in range(0, column_0):
            if mat_0[i][j] == 9:
                mat_1[i + 1][j + 1] = 1
            elif 0 <= mat_0[i][j] <= 8:
                mat_1[i + 1][j + 1] = 0
            elif mat_0[i][j] == -1:
                mat_1[i + 1][j + 1] = -1
    return mat_1



def method_1(row_0, column_0, mat_0, mat_1):
    list_mine = []
    list_nomine = []
    mat_3 = N.zeros((row_0, column_0, 8), dtype=int)
    for i in range(0, row_0):
        for j in range(0, column_0):
            mat_3[i][j][0] = mat_1[i][j]
            mat_3[i][j][1] = mat_1[i + 1][j]
            mat_3[i][j][2] = mat_1[i + 2][j]
            mat_3[i][j][3] = mat_1[i][j + 1]
            mat_3[i][j][4] = mat_1[i + 2][j + 1]
            mat_3[i][j][5] = mat_1[i][j + 2]
            mat_3[i][j][6] = mat_1[i + 1][j + 2]
            mat_3[i][j][7] = mat_1[i + 2][j + 2]
# print(mat_3[0][0])
            list_temp = mat_3[i][j].tolist()
            # print (list_temp)
            if mat_1[i + 1][j + 1] == 0 and list_temp.count(-1) != 0:
                # print(i, j)
                if mat_0[i][j] - list_temp.count(1) == list_temp.count(-1):
                    # print(i, j)
                    if mat_1[i][j] == -1:
                        list_mine.append((i - 1, j - 1))
                    if mat_1[i + 1][j] == -1:
                        list_mine.append((i, j - 1))
                    if mat_1[i + 2][j] == -1:
                        list_mine.append((i + 1, j - 1))
                    if mat_1[i][j + 1] == -1:
                        list_mine.append((i - 1, j))
                    if mat_1[i + 2][j + 1] == -1:
                        list_mine.append((i + 1, j))
                    if mat_1[i][j + 2] == -1:
                        list_mine.append((i - 1, j + 1))
                    if mat_1[i + 1][j + 2] == -1:
                        list_mine.append((i, j + 1))
                    if mat_1[i + 2][j + 2] == -1:
                        list_mine.append((i + 1, j + 1))
                elif mat_0[i][j] - list_temp.count(1) == 0:
                    print(i, j)
                    if mat_1[i][j] == -1:
                        list_nomine.append((i - 1, j - 1))
                    if mat_1[i + 1][j] == -1:
                        list_nomine.append((i, j - 1))
                    if mat_1[i + 2][j] == -1:
                        list_nomine.append((i + 1, j - 1))
                    if mat_1[i][j + 1] == -1:
                        list_nomine.append((i - 1, j))
                    if mat_1[i + 2][j + 1] == -1:
                        list_nomine.append((i + 1, j))
                    if mat_1[i][j + 2] == -1:
                        list_nomine.append((i - 1, j + 1))
                    if mat_1[i + 1][j + 2] == -1:
                        list_nomine.append((i, j + 1))
                    if mat_1[i + 2][j + 2] == -1:
                        list_nomine.append((i + 1, j + 1))
    return (list_mine, list_nomine)


    # if mat_1[i+1][j+1] == 0 or mat_1[i][j] != -1 or mat_1[i + 1][j] != -1 or mat_1[i + 2][j] != -1 or \
    #                 mat_1[i][j + 1] != -1 or mat_1[i + 2][j + 1] != -1 or mat_1[i][j + 2] != -1 or \
    #                 mat_1[i + 1][j + 2] != -1 or mat_1[i + 2][j + 2] != -1:
    #     list
    #             if abs(mat_1[i][j]) + abs(mat_1[i + 1][j]) + abs(mat_1[i + 2][j]) + abs(mat_1[i][j + 1]) + abs(mat_1[i + 2][j + 1]) + abs(mat_1[i][
    #                         j + 2]) + abs(mat_1[i + 1][j + 2])  + abs(mat_1[i + 2][j + 2]) == mat_0[i][j]:
    #                 if mat_1[i][j] == -1:
    #                     list_mine.append((i, j))
    #                 elif mat_1[i + 1][j] == -1:
    #                     list_mine.append((i + 1, j))
    #                 elif mat_1[i + 2][j] == -1:
    #                     list_mine.append((i + 2, j))
    #                 elif mat_1[i][j + 1] == -1:
    #                     list_mine.append((i, j + 1))
    #                 elif mat_1[i + 2][j + 1] == -1:
    #                     list_mine.append((i + 2, j + 1))
    #                 elif mat_1[i][j + 2] == -1:
    #                     list_mine.append((i, j + 2))
    #                 elif mat_1[i + 1][j + 2] == -1:
    #                     list_mine.append((i + 1, j + 2))
    #                 elif mat_1[i + 2][j + 2] == -1:
    #                     list_mine.append((i + 2, j + 2))
    # return list_mine

def csp(mat_0):
    (row_0, column_0) = N.shape(mat_0)
    mat_1 = matrix_expand(row_0, column_0, mat_0)
    # print(mat_1)
    (list_mine, list_nomine) = method_1(row_0, column_0, mat_0, mat_1)
    list_mine = N.unique(list_mine)
    list_nomine = N.unique(list_nomine)
    new_mine = []
    new_nomine = []
    for cell in list_mine:
        new_mine.append((cell[1], cell[0]))
    for cell in list_nomine:
        new_nomine.append((cell[1], cell[0]))
    return new_mine, new_nomine


# mat_0 = [[-1, 2, 1, 0], [3, 9, 1, 0], [9, 3, 2, 1], [-1, 2, 9, 1]]
# # mat_0 = [[-1, 2, 1, 0], [3, 9, 1, 0], [9, 3, 2, 1], [1, 2, 9, 1]]
# # mat_0 = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, 1]]
# a,b = csp(mat_0)
# print a
# print b






















