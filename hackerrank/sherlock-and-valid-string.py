#!/usr/bin/pyhon3
import sys

'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string
Sample input:
aabbcd
'''

def isValidString(expr):
	lowerCaseNum = [0] * 27
	base = ord('a')
	# use dict
	sample = ord(expr[0]) - base
	for ch in expr:
		lowerCaseNum[ord(ch) - base] += 1
	prevNum = 0
	sample3 = []
	for num in lowerCaseNum:
		if num != 0:
			sample3.append(num)
		if len(sample3) == 3:
			break

		if num == 0:
			continue
		else:
			if abs(sample - num) > 1:
				return False


if __name__ == "__main__":
	# isValidString(input())
	isValidString(sys.argv[1])