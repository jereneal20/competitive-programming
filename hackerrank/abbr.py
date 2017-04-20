#!/usr/bin/pyhon3
import sys

'''
https://www.hackerrank.com/challenges/abbr
Sample input:
1
daBcd
ABC
'''

def abbr(str1, str2):
    j = 0
    for i in range(len(str1)):
        if str2[j] == str1[i].upper():
            j += 1
        elif str1[i].isupper() == True:
            print("NO")
            return
        else: # str1이 lower라 무시해도 됨
            pass

        if len(str2) == j:
            print("YES")
            return
    print("NO")
    return


if __name__ == "__main__":
    f = open("input.txt","r")
    tc = int(f.readline())
    # tc = int(input())
    for i in range(tc):
        str1 = f.readline().strip()
        str2 = f.readline().strip()
        # str1 = input().strip()
        # str2 = input().strip()
        abbr(str1, str2)