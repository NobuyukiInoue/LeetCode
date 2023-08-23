import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # 169ms - 171ms
        n = len(arr)
        dp = [0]*n
        dp[0] = max_val = arr[0]
        for i in range(1, k):
            max_val = max(max_val, arr[i])
            dp[i] = max_val*(i + 1)
        for i in range(k, n):
            max_val = arr[i]
            for j in range(1, k + 1):
                max_val = max(max_val, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + max_val*j)
        return dp[n - 1]

    def maxSumAfterPartitioning1(self, arr: List[int], k: int) -> int:
        # 146ms - 153ms
        n, dp = len(arr), list(arr)
        max_val = arr[0]
        for i in range(1, k):
            if arr[i] > max_val:
                max_val = arr[i]
            dp[i] = max_val*(i + 1)
        maxs = [[0]*(k + 1) for _ in range(n)]
        for i in range(n - 1, k - 2, -1):
            mval = arr[i]
            for j in range(k + 1):
                mval = max(mval, arr[i - j])
                maxs[i][j] = mval*(j + 1)
        for i in range(k, n):
           dp[i] = max([maxs[i][j - 1] + dp[i - j] for j in range(1, k + 1)])
        return dp[n - 1]

    def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
        # 858ms - 886ms
        dp = {}
        def df(idx: int, arr: List[int], n: int, maxs: List[int], size: int) -> int:
            if idx == n:
                return maxs * size  
            if (idx, size, maxs) in dp:
                return dp[(idx, size, maxs)]
            ch1 = df(idx + 1, arr, n, max(maxs,arr[idx]), size + 1) if size < k else 0
            ch2 = df(idx + 1, arr, n, arr[idx], 1) + maxs*size
            best = ch1 if ch1 > ch2 else ch2
            dp[(idx, size, maxs)] = best
            return best
        return df(1, arr, len(arr), arr[0], 1)

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    arr = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("arr = {0}, k = {1:d}".format(arr, k))

    sl = Solution()
    time0 = time.time()

    result = sl.maxSumAfterPartitioning(arr, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
