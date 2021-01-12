# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1500ms
        q, res = collections.deque(), []
        for i, num in enumerate(nums):
            if i - k >= 0:
                res.append(nums[q[0]])
                while q and q[0] <= i - k:
                    q.popleft()
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res

    def maxSlidingWindow_normal(self, nums: List[int], k: int) -> List[int]:
        # Time Limite Exceeded.
        res = []
        currentMax = max(nums[:k])
        res.append(currentMax)
        for i in range(1, len(nums) - k + 1):
            if nums[i + k - 1] > currentMax:
                currentMax = nums[i + k - 1]
            elif nums[i - 1] == currentMax:
                currentMax = max(nums[i:i + k])
            res.append(currentMax)
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
    nums, k = [int(n) for n in flds[0].split(",")], int(flds[1])
    print("nums = {0}, k = {1}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.maxSlidingWindow(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
