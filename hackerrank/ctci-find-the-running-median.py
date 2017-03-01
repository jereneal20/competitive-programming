#!/bin/python3

'''
https://www.hackerrank.com/challenges/ctci-find-the-running-median
Sample input:
6
12
4
5
3
8
7
'''

import bisect
import sys

def find_the_running_median(num, inputs):
    medianArr = []
    for elem in inputs:
        bisect.insort(medianArr, elem)
        if len(medianArr) % 2 == 0:
            print((medianArr[int(len(medianArr)/2)] + medianArr[int(len(medianArr)/2)-1])/2)
        else:
            print(float(medianArr[int(len(medianArr)/2)]))

if __name__ == "__main__":
    n = int(input().strip())
    # n = int(sys.argv[1])
    a = []
    for iter in range(n):
        a_i = int(input().strip())
        a.append(a_i)
        # a.append(int(sys.argv[iter + 2]))
    find_the_running_median(n, a)



