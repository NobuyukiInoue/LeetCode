# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # 112ms
        arr.sort()
        lookup = {arr[-1]}
        factor_dict = {}
        for i in range(0, len(arr)-1)[::-1]:
            for j in range(i+1):
                if arr[i]*arr[j] > arr[-1]:
                    break
                if arr[i]*arr[j] in lookup:
                    if i != j:
                        factor_dict[arr[i]*arr[j]] = factor_dict.get(arr[i]*arr[j], []) + [arr[i], arr[j]]
                    else:
                        factor_dict[arr[i]**2] = factor_dict.get(arr[i]**2, []) + [arr[i]]
            lookup.add(arr[i])
        for n in arr:
            if n not in factor_dict:
                factor_dict[n] = 1
                continue
            idx, total = 0, 0
            while idx < len(factor_dict[n]):
                if factor_dict[n][idx]**2 == n:
                    total += factor_dict[factor_dict[n][idx]]*factor_dict[factor_dict[n][idx]]
                    idx += 1
                else:
                    total += 2*factor_dict[factor_dict[n][idx]]*factor_dict[factor_dict[n][idx+1]]
                    idx += 2
            factor_dict[n] = total + 1
        return sum(factor_dict.values()) % (10**9 + 7)  

    def numFactoredBinaryTrees2(self, arr: List[int]) -> int:
        # 320ms
        dp = {}
        for a in sorted(arr):
            dp[a] = sum(dp[b] * dp.get(a / b, 0) for b in dp if a % b == 0) + 1
        return sum(dp.values()) % (10**9 + 7)

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()

    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()

    time0 = time.time()

    result = sl.numFactoredBinaryTrees(arr)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
