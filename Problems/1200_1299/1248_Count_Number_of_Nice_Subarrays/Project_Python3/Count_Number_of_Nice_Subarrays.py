# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 808ms
        inds = [i for i,x in enumerate(nums) if x&1]
        La, Li = len(nums), len(inds)
        res  = 0
        for i in range(len(inds) - k + 1):
            a = inds[i]
            b = inds[i + k - 1]
            prev = inds[i - 1] if i > 0 else -1
            last = inds[i + k] if (i + k) < Li else La
            res += (a - prev)*(last - b)
        return res

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        # 896ms
        def subarraySumEqualsk(nums, k):
            total, count =0, 0
            dict1 = {0:1}
            prefixSum = [0]*len(nums)
            for i in range(len(nums)):
                total += nums[i]
                if total not in dict1:
                    dict1[total] = 0
                dict1[total] += 1
                if total - k in dict1:
                    count += dict1[total - k]
                prefixSum[i] = total
            return count
        
        for i in range(len(nums)):
            nums[i] = 0 if nums[i]%2 == 0 else 1
        return subarraySumEqualsk(nums, k)

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

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfSubarrays(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
