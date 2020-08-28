# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def combinationSum3(self, k, n):
        # 32m
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res
        
    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)

    def combinationSum3_2(self, k, n: int):
        # 32ms
        def sub_combinationSum3(k, n, i, temp):
            if k == 1:
                if n < 10:
                    temp[len(temp) - 1] = n
                    res.append(temp.copy())
                return
            for j in range(i, n - k + 1):
                temp[len(temp) - k] = j
                if j >= n - j:
                    break
                if j >= 10:
                    break
                sub_combinationSum3(k - 1, n - j, j + 1, temp.copy())
            return

        res = []
        temp = [0 for _ in range(k)]
        for i in range(1, n - k + 1):
            temp[0] = i
            if i >= n - i:
                break
            if i >= 10:
                break
            sub_combinationSum3(k - 1, n - i, i + 1, temp.copy())

        return res


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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    k, n = int(flds[0]), int(flds[1])
    print("k = {0:d}, n = {1:d}".format(k, n))

    sl = Solution()
    time0 = time.time()

    result = sl.combinationSum3(k, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
