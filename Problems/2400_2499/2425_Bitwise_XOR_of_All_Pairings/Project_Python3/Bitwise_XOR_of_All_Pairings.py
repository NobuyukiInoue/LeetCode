import functools
import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 458ms - 484ms
        return functools.reduce(operator.xor, nums1*(len(nums2)&1) + nums2*(len(nums1)&1), 0)

    def xorAllNums2(self, nums1: List[int], nums2: List[int]) -> int:
        # 483ms - 491ms
        return (functools.reduce(operator.xor, nums1) if len(nums2)%2 else 0) ^ (functools.reduce(operator.xor, nums2) if len(nums1)%2 else 0)

    def xorAllNums3(self, nums1: List[int], nums2: List[int]) -> int:
        # 472ms - 473ms
        x = y = 0
        for num1 in nums1:
            x ^= num1
        for num2 in nums2:
            y ^= num2
        return (len(nums1)%2*y)^(len(nums2)%2*x)

    def xorAllNums_bad(self, nums1: List[int], nums2: List[int]) -> int:
        # Time Limite Exceeded 36/42.
        ans = 0
        for num1 in nums1:
            for num2 in nums2:
                ans ^= num1 ^ num2
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums1 = [int(col) for col in flds[0].split(",")]
    nums2 = [int(col) for col in flds[1].split(",")]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.xorAllNums(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
