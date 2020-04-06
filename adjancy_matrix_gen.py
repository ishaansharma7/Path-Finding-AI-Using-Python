# def relation(l, r):
#     vertical = 20
#     vertical_rem = 19
#     diagonal1 = 19
#     diagonal2 = 21
#     if l == r:
#         return 0
#     if l%vertical != 0 and l%vertical!=vertical_rem:  # check not leftest or rightest column
#         if l+1==r or l-1==r or l+vertical==r or l-vertical==r:
#             return 1
#         elif l+diagonal1==r or l-diagonal1==r or l+diagonal2==r or l-diagonal2==r:
#             return 1.5
#         else:
#             return 0
#     elif l%vertical==0:
#         if l+1==r or l+vertical==r or l-vertical==r:
#             return 1
#         elif l-diagonal1==r  or l+diagonal2==r:
#             return 1.5
#         else:
#             return 0
#     elif l%vertical==vertical_rem:
#         if l-1==r or l+vertical==r or l-vertical==r:
#             return 1
#         elif l+diagonal1==r or l-diagonal2==r:
#             return 1.5
#         else:
#             return 0

def relation(l, r):
    vertical = 20
    vertical_rem = 19
    diagonal1 = 19
    diagonal2 = 21
    if l == r:
        return 0
    if l%vertical != 0 and l%vertical!=vertical_rem:  # check not leftest or rightest column
        if l+1==r or l-1==r or l+vertical==r or l-vertical==r:
            return 1

        else:
            return 0
    elif l%vertical==0:
        if l+1==r or l+vertical==r or l-vertical==r:
            return 1

        else:
            return 0
    elif l%vertical==vertical_rem:
        if l-1==r or l+vertical==r or l-vertical==r:
            return 1

        else:
            return 0

row_col_size = 20
size = row_col_size*row_col_size
adjancey_mat = [[0 for i in range(size)] for j in range(size)]

for i in range(0, size):
    for j in range(0, size):
        result = relation(i,j)
        adjancey_mat[i][j] = result

def return_matrix():
    return adjancey_mat, size



# for i in range(0, 100):
#     for j in range(0, 100):
#         print(adjancey_mat[i][j], end=',')
#     print()
#
# print(adjancey_mat[99][90])