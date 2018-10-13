"""
Find the hourglass that has the max sum
"""

import math
import os
import random
import re
import sys

HOURGLASS_SET = [
    (1, 0), (2, 0),
    (1, 1),
    (0, 2), (1, 2), (2, 2)
]

def getHourglassSum(col, row, arr):
    sum = arr[row][col]
    for hgCell in HOURGLASS_SET:
        hgColNo, hgRowNo = hgCell
        newCol = col + hgColNo
        newRow = row + hgRowNo
        if newCol > 5 or newRow > 5:
            return -63
        sum += arr[newRow][newCol]

    return sum

def hourglassSum(arr):
    maxHourglassSum = -63 # -9 * number of elements in an hour glass
    for rowNo, row in enumerate(arr):
        for colNo, cellValue in enumerate(row):
            sum = getHourglassSum(colNo, rowNo, arr)
            if sum > maxHourglassSum:
                maxHourglassSum = sum

    return maxHourglassSum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
