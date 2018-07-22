# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000)

def ethan_traverses(trie_arr, K):
    preorder_list = []
    postorder_list = []

    def preorder_traverse(tree_dict, idx):
        if idx == 0:
            return
        preorder_list.append(idx)
        preorder_traverse(tree_dict, tree_dict[idx][0])
        preorder_traverse(tree_dict, tree_dict[idx][1])

    def postorder_traverse(tree_dict, idx):
        if idx == 0:
            return
        postorder_traverse(tree_dict, tree_dict[idx][0])
        postorder_traverse(tree_dict, tree_dict[idx][1])
        postorder_list.append(idx)

    tree_dict = dict()
    for i in range(len(trie_arr)):
        tree_dict[i+1] = trie_arr[i]

    preorder_traverse(tree_dict, 1)
    postorder_traverse(tree_dict, 1)

    arr = [0] * (K + 1)
    for m in range(len(arr)):
        arr[m] = list()
    arr[1].append(1)
    used_k = 1

    for iter in range(len(preorder_list)):
        if preorder_list[iter] == -1:
            continue
        idx = iter
        while True:
            if postorder_list[idx] not in arr[used_k]:
                arr[used_k].append(postorder_list[idx])
            idx = preorder_list.index(postorder_list[idx])
            preorder_list[idx] = -1
            if postorder_list[idx] in arr[used_k]:
                used_k += 1
                if used_k > K:
                    used_k = 1
                break

    for iter in range(1, len(arr)):
        if not arr[iter]:
            return "Impossible"
    result_arr = [0] * (len(preorder_list) + 1)
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            result_arr[arr[i][j]] = i
    return_str = " ".join(str(x) for x in result_arr[1:])

    return return_str


if __name__ == "__main__":
    f = open("ethan_traverses_a_tree.txt", "r")
    out = open("ethan-output.txt", "w")
    tc = int(f.readline())
    for i in range(tc):
        N, K = [int(i) for i in f.readline().split(' ')]
        trie_arr = [0] * N
        for k in range(N):
            trie_arr[k] = [int(j) for j in f.readline().split(' ')]
        ret = ethan_traverses(trie_arr, K)

        out.write("Case #%d: %s\n" % (i + 1, ret))
        print("Case #%d: %s" % (i + 1, ret))
    out.close()
