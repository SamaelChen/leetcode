import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb


def find_smallest(arr):
    smallest_elm = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_elm:
            smallest_elm = arr[i]
    return smallest_elm


def selection_sort(arr):
    newArr = []
    while len(arr) > 0:
        elm = find_smallest(arr)
        newArr.append(elm)
        arr.remove(elm)
    return newArr


s = [5, 3, 6, 2, 10]
selection_sort(s)


def sum_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])


s = [1, 2, 3, 4, 5, 6]
sum_arr(s)


def factory(n):
    if n == 1:
        return 1
    else:
        return n * factory(n - 1)


factory(4)


def hail(n):
    print(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    if n == 1:
        return 1
    else:
        return hail(n)


hail(199)

y + 192)!@BJ
xL00Kts@nightky
