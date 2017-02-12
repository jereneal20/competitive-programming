#!/usr/bin/pyhon3
import sys
from operator import itemgetter

'''
https://www.hackerrank.com/challenges/sherlock-and-minimax
Sample input:
3
5 8 14
4 9
'''


def getminimax(p, q, a):
	a.sort()
	if q <= a[0]:
		return p
	if p >= a[len(a) - 1]:
		return q
	solIsP = min([abs(tmp - p) for tmp in a])
	solIsQ = min([abs(tmp - q) for tmp in a])

	pairList = []
	for idx, num in enumerate(a):
		if idx + 1 != len(a):
			delta = int((a[idx + 1] - a[idx]) / 2)
			if a[idx] + delta < p:
				pairList.append([solIsP, p])
			elif a[idx] + delta > q:
				pairList.append([solIsQ, q])
			else:
				pairList.append([delta, a[idx] + delta])
	if a[len(a) - 1] < q:
		pairList.append([solIsQ, q])
	if a[0] > p:
		pairList.append([solIsP, p])

	tmp = max(pairList, key=itemgetter(0))
	result = [lists[1] for lists in pairList if tmp[0] == lists[0]]
	return min(result)


if __name__ == "__main__":
	n = int(input())
	a = [int(str) for str in input().split()]
	p, q = input().split()
	p = int(p)
	q = int(q)
	# n = int(sys.argv[1])
	# a = []
	# iter = 0
	# for iter in range(n):
	# 	a.append(int(sys.argv[iter+2]))
	# p = int(sys.argv[iter + 3])
	# q = int(sys.argv[iter + 4])
	print(getminimax(p, q, a))