#!/usr/bin/pyhon3
import sys

'''
Sample input:
SALLY
HARRY
'''

def common_child(str1, str2):
	prevArr = [0] * (len(str1) + 1)
	curArr = [0] * (len(str1) + 1)
	for c1 in str1:
		for j, c2 in enumerate(str2):
			if c1 == c2:
				curArr[j] = prevArr[j - 1] + 1
			else:
				if prevArr[j] > curArr[j - 1]:
					curArr[j] = prevArr[j]
				else:
					curArr[j] = curArr[j - 1]
		curArr, prevArr = prevArr, curArr
	print(prevArr[-2])


if __name__ == "__main__":
	# str1 = input()
	# str2 = input()
	# main(str1, str2)
	common_child(sys.argv[1], sys.argv[2])