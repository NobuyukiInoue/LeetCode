import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 376ms
        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]
        return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]

    def xorQueries2(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 384ms
        xorList = [0]*(len(arr) + 1)
        for i in range(len(arr)):
            xorList[i + 1] = xorList[i]^arr[i]
        res = []
        for q in queries:
            l, r = q[0], q[1]
            res.append(xorList[l]^xorList[r + 1])
        return res

    def xorQueries3(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 384ms
        if len(queries) == 0:
            return []
        n = len(arr)
        xorList = [0]*n
        xorList[0] = arr[0]
        for i in range(1, n):
            xorList[i] = xorList[i - 1]^arr[i]
        ans = [0]*len(queries)
        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1]
            if l == 0:
                ans[i] = xorList[r]
            else:
                ans[i] = xorList[r]^xorList[l - 1]
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
    flds = temp.replace(", ",",").replace("\"","").replace("]]]","").rstrip().split("],[[")

    arr = [int(_) for _ in flds[0].replace("[[", "").split(",")]
    queries = [[int(data) for data in item.split(",")] for item in flds[1].split("],[")]
    print("arr = {0}, queries = {1}".format(arr, queries))

    sl = Solution()
    time0 = time.time()

    result = sl.xorQueries(arr, queries)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
