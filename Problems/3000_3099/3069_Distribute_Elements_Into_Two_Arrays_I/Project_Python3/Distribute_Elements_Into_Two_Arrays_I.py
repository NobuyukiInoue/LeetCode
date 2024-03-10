import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # 41ms - 45ms
        arr1, arr2 = [nums[0]], [nums[1]]
        last1, last2 = arr1[0], arr2[0]
        for num in nums[2:]:
            if last1 > last2:
                arr1.append(num)
                last1 = num
            else:
                arr2.append(num)
                last2 = num
        return arr1 + arr2

    def resultArray2(self, nums: List[int]) -> List[int]:
        # 48ms - 52ms
        arr1, arr2 = [nums[0]], [nums[1]]
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2

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
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.resultArray(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
