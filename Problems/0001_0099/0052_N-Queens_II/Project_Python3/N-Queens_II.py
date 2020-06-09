# coding: utf-8

import copy
import os
import sys
import time
import itertools

class Solution:
#   def totalNQueens(self, n: int) -> int:
    def totalNQueens(self, n):
        # 52ms
        res = []
        def dfs(i, l, r, m, arr):
            if i == n:
                res.append(arr)
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m, arr + [("." * j) + "Q" + ("." * (n - j - 1))])
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n, [])
        return len(res)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.totalNQueens(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()
