# -*- coding: utf-8 -*-


def tourist(k, v, attractions):
    ret_list = []
    start_attr_num = (k * (v - 1)) % len(attractions)
    i = 0
    tmp_idx_list = []
    while i < k:
        tmp_idx_list.append((i + start_attr_num) % len(attractions))
        i += 1
    tmp_idx_list.sort()
    for idx in tmp_idx_list:
        ret_list.append(attractions[idx])
    return ret_list


if __name__ == "__main__":
    f = open("tourist.txt", "r")
    out = open("tourist-output.txt", "w")
    tc = int(f.readline())
    # tc = int(input())
    for i in range(tc):
        n, k, v = f.readline().strip().split(' ')
        n, k, v = int(n), int(k), int(v)
        attractions = []
        for line in range(n):
            str2 = f.readline().strip()
            attractions.append(str2)
        ret_list = tourist(k, v, attractions)
        out.write("Case #%d: %s\n" % (i+1, ' '.join(ret_list)))
        print("Case #%d: %s" % (i+1, ' '.join(ret_list)))
    out.close()
