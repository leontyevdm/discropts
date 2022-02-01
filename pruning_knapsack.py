import sys
import numpy as np
from time import time
sys.setrecursionlimit(100000)

def Linprog_solution(values, weights, free_weight):
    sorted = np.argsort(-values/weights)
    cur_weight = 0
    cur_value = 0
    for i in sorted:
        if cur_weight + weights[i] <= free_weight:
            cur_value += values[i]
            cur_weight += weights[i]
        else:
            cur_value += values[i]*(free_weight-cur_weight)/weights[i]
            break
    return cur_value

def greedy(values, weights, total_weight):
    specific_sorted = np.argsort(-values/weights)
    specific_cur_weight = 0
    specific_cur_value = 0
    specific_visited = np.zeros(values.size)
    for el in specific_sorted:
        if specific_cur_weight + weights[el] <= total_weight:
            specific_visited[el] = 1
            specific_cur_value += values[el]
            specific_cur_weight += weights[el]
        elif weights[el] <= total_weight:
            specific_cur_value = max(specific_cur_value, values[el])
            if specific_cur_value == values[el]:
                specific_visited = np.zeros(values.size)
                specific_visited[el] = 1
            break
    return specific_cur_value, specific_visited


def solve_knapsack(values, weights, free_weight, price, visited):
    global start
    if time() - start > 28:
        return
    global opt
    if values.size != 0:
        if visited[0]:
            solve_knapsack(values[1:], weights[1:], free_weight - weights[0], price + values[0], visited[1:])
            upper_bound = Linprog_solution(values[1:], weights[1:], free_weight) + price
            if upper_bound > opt:
                greedy0, visited0 = greedy(values[1:], weights[1:], free_weight)
                opt = max(opt, greedy0 + price)
                solve_knapsack(values[1:], weights[1:], free_weight, price, visited0)
        else:
            solve_knapsack(values[1:], weights[1:], free_weight, price, visited[1:])
            if weights[0] <= free_weight:
                upper_bound = Linprog_solution(values[1:], weights[1:], free_weight - weights[0])
                upper_bound += (price + values[0])
                if upper_bound > opt:
                    greedy1, visited1 = greedy(values[1:], weights[1:], free_weight - weights[0])
                    opt = max(opt, greedy1 + price + values[0])
                    solve_knapsack(values[1:], weights[1:], free_weight - weights[0], price + values[0], visited1)



total_weight = int(input())
n = int(input())
start = time()
values = np.zeros(n)
weights = np.zeros(n)

for i in range(n):
    next = list(map(int, input().split()))
    weights[i] = next[0]
    values[i] = next[1]

opt, visited = greedy(values,weights,total_weight)
solve_knapsack(values,weights,total_weight,0,visited)
print(int(opt))
