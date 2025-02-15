import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # 82ms - 94ms
        cnt, pre_max_cnt, res = 1, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                pre_max_cnt, cnt = cnt, 1
            res = max(res, cnt//2, min(pre_max_cnt, cnt))
        return res >= k

    def hasIncreasingSubarrays2(self, nums: List[int], k: int) -> bool:
        # 82ms - 84ms
        def mono(idx: int)-> bool:
            for i in range(idx, idx + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        for idx in range(len(nums) - k - k + 1):
            if mono(idx) and mono(idx + k):
                return True
        return False

    def hasIncreasingSubarrays3(self, nums: List[int], k: int) -> bool:
        # 87ms - 94ms
        def isStrictlyIncreasing(nums: List[int], start: int, k: int):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        n = len(nums)
        if n < 2 * k:
            return False
        for i in range(n - 2 * k + 1):
            if isStrictlyIncreasing(nums, i, k) and isStrictlyIncreasing(nums, i + k, k):
                return True
        return False

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    nums, k = [int(num) for num in flds[0].split(",")], int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.hasIncreasingSubarrays(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
