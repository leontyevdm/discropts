import numpy as np
import scipy.optimize as sci
import random


n_columns, n_rows = map(int, input().split())
M = np.zeros((n_rows, n_columns))
w = np.zeros(n_rows)

for i in range(n_rows):
    row = list(map(int, input().split()))
    w[i] = row[0]
    for j in range(1, len(row)):
        M[i][row[j]] = 1

def linprog_solution(M, w):
    b = -np.ones(len(M.T))
    res = sci.linprog(c=w, A_ub=-M.T, b_ub=b, bounds=(0, 1))
    return res.x

def probability_round(M, x):
    rounded = np.zeros(len(x))
    one_matrix = np.ones(len(M.T))
    order = np.flip(np.argsort(x), axis=0)
    while (M.T @ rounded < one_matrix).any():
        for i in order:
            if not rounded[i]:
                coin = random.random()
                if coin < x[i]:
                    rounded[i] = 1
                    break
    return rounded

lin = linprog_solution(M,w)
x = probability_round(M, lin)
for i in range(len(x)):
    if x[i] > 0:
        print(i + 1, end=' ')
