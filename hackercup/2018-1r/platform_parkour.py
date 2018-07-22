# -*- coding: utf-8 -*-


def platform_parkour(arr, nol):
    if nol % 2 == 1:
        return 0
    if '#' in arr[1]:
        return 0
    for idx in range(nol):
        if arr[0][idx] == arr[2][idx] == '#':
            return 0
    if arr[0][0] == '#' or arr[1][0] == '#':
        return 0
    if nol >= 2 and (arr[1][-1] == '#' or arr[2][-1] == '#'):
        return 0

    idx = 1
    count = 1
    while idx < nol - 1:
        if arr[0][idx] == '#' and arr[2][idx + 1] == '#':
            return 0
        if arr[2][idx] == '#' and arr[0][idx + 1] == '#':
            return 0
        if arr[0][idx] == '#' or arr[2][idx] == '#' or \
            arr[0][idx + 1] == '#' or arr[2][idx + 1] == '#':
            pass
        else:
            count *= 2
        count %= 1000000007
        idx += 2

    return count


if __name__ == "__main__":
    f = open("input.txt", "r")
    out = open("parkour-output.txt", "w")
    tc = int(f.readline())
    for i in range(tc):
        N, M = f.readline().split(' ')
        N = int(N)
        M = int(M)
        H = [0] * (N + 1)
        l = f.readline().split(' ')
        H[1], H[2], W, X, Y, Z = [int(i) for i in l]
        
        for j in range(M):
            l2 = f.readline().split(' ')

            arr[j] = f.readline().strip()
        ret = let_it_flow(arr, nol)

        out.write("Case #%d: %s\n" % (i + 1, ret))
        print("Case #%d: %s" % (i + 1, ret))
    out.close()
