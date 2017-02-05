#!/usr/bin/pyhon3
import sys

'''
Sample input:
3
{[()]}
{[(])}
{{[[(())]]}}
'''

def balanced_brackets(expr):
	stack = []
	for c in expr:
		if c == "(" or c == "{" or c == "[":
			stack.append(c)
		else:
			if not stack:
				return False
			popped = stack.pop()
			if popped == "(" and c == ")" or \
				popped == "{" and c == "}" or \
				popped == "[" and c == "]":
				pass
			else:
				return False
	if not stack:
		return True
	else:
		return False


if __name__ == "__main__":
	# n = int(input())
	n = int(sys.argv[1])
	for i in range(0, n):
		expr = sys.argv[i + 2]
		# str = input()
		if balanced_brackets(expr) == True:
			print("YES")
		else:
			print("NO")