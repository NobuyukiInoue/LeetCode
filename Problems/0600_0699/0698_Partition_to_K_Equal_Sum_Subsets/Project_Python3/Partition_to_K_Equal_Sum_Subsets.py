# coding: utf-8

import json
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 64ms
        total = 0
        for num in nums:
            total += num
        if k <= 0 or total % k != 0:
            return False
        def dfs(nums: List[int], visited: List[bool], startIndex: int, k: int, currentSum: int, target: int):
            if k == 1:
                return True
            if currentSum > target:
                return False
            if currentSum == target:
                return dfs(nums, visited, 0, k - 1, 0, target)
            for i in range(startIndex, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if dfs(nums, visited, i + 1, k, currentSum + nums[i], target):
                        return True
                    visited[i] = False
            return False
        visited = [False]*len(nums)
        return dfs(nums, visited, 0, k, 0, total//k)

    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        # 44ms
        sums = [0]*k
        subsum = sum(nums) // k
        nums.sort(reverse=True)
        l = len(nums)
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i + 1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False
        return walk(0)

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
    nums, k = [int(n) for n in flds[0].split(",")], int(flds[1])
    print("nums = {0}, k = {1}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.canPartitionKSubsets(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
