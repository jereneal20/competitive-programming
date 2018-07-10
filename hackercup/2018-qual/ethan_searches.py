# -*- coding: utf-8 -*-


def generate_tc(input_str):
    first_char = input_str[0]
    occurs = [i for i, x in enumerate(input_str) if x == first_char]
    if len(occurs) == 1:
        return "Impossible"
    for idx in occurs[1:]:
        iter_str = input_str[:idx]
        tmp_idx = idx
        while tmp_idx < len(input_str):
            if iter_str[tmp_idx % idx] == input_str[tmp_idx]:
                tmp_idx += 1
            else:
                break
        if tmp_idx == len(input_str):
            return "Impossible"
        return input_str[:idx] + input_str

if __name__ == "__main__":
    f = open("ethan_searches_for_a_string.txt", "r")
    out = open("ethan-output2.txt", "w")
    tc = int(f.readline())
    # tc = int(input())
    for i in range(tc):
        input_str = f.readline().strip()
        ret = generate_tc(input_str)

        out.write("Case #%d: %s\n" % (i + 1, ret))
        print("Case #%d: %s" % (i + 1, ret))
    out.close()
