# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def combine(self, n: int, k: int) -> List[List[int]]:
    def combine2(self, n, k):
        # 544ms
        ans = []
        def dfs(n, count, cur, i, j, ans):
            if i == count:
                ans.append(cur[:])
            for x in range(j, n + 1):
                dfs(n, count, cur + [x], i + 1, x + 1, ans)
        dfs(n, k, [], 0, 1, ans)
        return ans

    def combine(self, n, k):
        # 96ms
        ans, stack = [], []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return ans

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    n, k = int(flds[0]), int(flds[1])
    print("n = {0:d}, k = {1:d}".format(n, k))

    sl = Solution()

    time0 = time.time()

    result = sl.combine(n, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
