import numpy as np
import math


def basic_check(column):
    return column.tolist().count(1) == 1 and column.tolist().count(0) == len(column) - 1


def solution(table):
    columns = np.array(table).T
    solutions = []

    for column in range(len(columns) - 1):
        cur_solution = 0
        if basic_check(columns[column]):
            index_of_one = columns[column].tolist().index(1)
            cur_solution = columns[-1][index_of_one]
        solutions.append(cur_solution)

    return solutions


def iteration(table, pivot_position):
    new_table = []

    for i in range(len(table)):
        new_table.append([])

    i, j = pivot_position
    pivot_value = table[i][j]
    new_table[i] = np.array(table[i]) / pivot_value

    for k in range(len(table)):
        if k != i:
            new_table[k] = np.array((table[k])) - np.array(new_table[i]) * table[k][j]

    return new_table


def get_pivot_position(table):
    row = table[-1]
    column_i = 0  # be careful

    for i in range(len(row) - 1):
        if row[i] > 0:
            column_i = i
            break

    restrictions = []

    for i in range(len(table) - 1):
        if table[i][column_i] <= 0:
            restrictions.append(math.inf)
        else:
            restrictions.append(table[i][-1] / table[i][column_i])

    row_i = restrictions.index(min(restrictions))

    return row_i, column_i


def poss_to_enhance(table):
    row = table[-1]
    found = False

    for x in range(len(row) - 1):
        if row[x] > 0:
            found = True
            break

    return found


def make_table(c, A, b):
    for i in range(len(A)):
        for j in range(len(A)):
            if j == i:
                A[i].append(1)
            else:
                A[i].append(0)

    for i in range(len(A)):
        c.append(0)

    Ab = []
    for i in range(len(A)):
        Ab.append(A[i] + [b[i]])

    last_row = c + [0]
    return Ab + [last_row]


def simplex_method(c, A, b):
    table = make_table(c, A, b)

    while poss_to_enhance(table):
        pivot_position = get_pivot_position(table)
        table = iteration(table, pivot_position)

    return solution(table)


def approx(op, accuracy):
    for k in range(len(op)):
        op[k] = round(op[k], accuracy)
    return op


def calc_final_value(op, c):
    x = 0
    for k in range(len(op)):
        x += op[k] * c[k]
    return x


def solve(c, A, b, ap):

    output = approx(simplex_method(c, A, b), ap)
    value = round(calc_final_value(simplex_method(c, A, b), c), ap)

    return output, value


def get_user_input():
    print("Write input in this form:\n"
          "number_of_variables_in_objective_function number_of_inequalities_in_subject\n"
          "vector of coefficients of objective function\n"
          "matrix of coefficients of constraint function\n"
          "vector of right-hand side numbers\n"
          "approximation accuracy")

    num_columns, num_rows = list(map(int, input().split()))

    c = list(map(int, input().split()))

    A = []

    for i in range(num_rows):
        A.append(list(map(int, input().split())))

    b = list(map(int, input().split()))
    ap = int(input())

    for i in range(len(A)):
        flag = False
        for j in range(len(A[i])):
            if A[i][j] > 0:
                flag = True
                break
        if not flag:
            print("The method is not applicable")

    for i in b:
        if i < 0:
            print("The method is not applicable")
            exit(0)

    return c, A, b, ap


if __name__ == "__main__":
    c, A, b, ap = get_user_input()

    output, value = solve(c, A, b, ap)

    print(output)
    print(value)
