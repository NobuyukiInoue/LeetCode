import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 36ms - 52ms
        s = cnt = 0
        goal = (1 << (k + 1)) - 2
        while nums:
            cnt += 1
            if (num := nums.pop()) <= k:
                s |= (1 << num)
            if s == goal:
                return cnt

    def minOperations1(self, nums: List[int], k: int) -> int:
        # 45ms - 46ms
        left = (1 << k) - 1
        for i, num in enumerate(reversed(nums)):
            if num <= k and left & 1 << num - 1:
                left ^= 1 << num - 1
            if left == 0:
                return i + 1

    def minOperations3(self, nums: List[int], k: int) -> int:
        # 40ms - 42ms
        check = [0]*(k + 1)
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                if check[nums[i]] == 0:
                    check[nums[i]] = 1
                    cnt += 1
                    if cnt == k:
                        return len(nums) - i
        return len(nums) - i

    def minOperations4(self, nums: List[int], k: int) -> int:
        # 42ms - 52ms
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            j = abs(nums[i]) - 1
            if j < k and nums[j] > 0:
                cnt += 1
                nums[j] *= -1
                if cnt == k:
                    return len(nums) - i

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

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.minOperations(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
