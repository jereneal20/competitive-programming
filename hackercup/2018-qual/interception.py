# -*- coding: utf-8 -*-


def interception(polynomials):
    init_pow = 0
    for idx in range(0, len(polynomials)):
        if init_pow == 0:
            init_pow = 1
        else:
            init_pow = 0
    if init_pow == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    f = open("interception.txt", "r")
    out = open("interception-output.txt", "w")
    tc = int(f.readline())
    # tc = int(input())
    for i in range(tc):
        n = int(f.readline().strip())
        polynomials = []
        for idx in range(n + 1):
            polynomials.append(int(f.readline().strip()))

        ret = interception(polynomials)
        if ret:
            out.write("Case #%d: %s\n%s\n" % (i + 1, '1', '0'))
        else:
            out.write("Case #%d: %s\n" % (i + 1, "0"))
    out.close()
