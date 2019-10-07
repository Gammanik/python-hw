# #!/usr/bin/env python3


def matrix_product(a_rows, b_rows):
    res = [[0 for y in range(len(b_rows[0]))] for x in range(len(a_rows))]

    if len(a_rows) == 0 or len(b_rows[0]) == 0 or len(a_rows[0]) != len(b_rows):
        raise ValueError("Invalid matrix size")

    for i in range(len(a_rows)):
        for j in range(len(b_rows[0])):
            for k in range(len(b_rows)):
                res[i][j] += a_rows[i][k] * b_rows[k][j]

    return res


def matrix_pretty_print(mat):
    for i in range(0, len(mat)):
        row_str = ""
        row_div = "-"

        for j in range(0, len(mat[0])):
            row_str += "|\t" + str(mat[i][j]) + "\t"
        row_str += "|"
        row_str = row_str.expandtabs()
        for k in range(0, len(row_str)):
            row_div += "-"
        print(row_div)
        print(row_str)

    print(row_div)
    return
