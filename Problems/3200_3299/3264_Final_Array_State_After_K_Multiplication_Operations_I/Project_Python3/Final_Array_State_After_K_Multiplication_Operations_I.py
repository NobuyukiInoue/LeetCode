import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # 70ms
        while k > 0:
            n, v_min = 0, sys.maxsize
            for i, num in enumerate(nums):
                if num < v_min:
                    n, v_min = i, num
            nums[n] *= multiplier
            k -= 1
        return nums

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
    
    nums, k, multiplier = [int(num) for num in flds[0].split(",")], int(flds[1]), int(flds[2])
    print("nums = {0}, k = {1:d}, multiplier = {2:d}".format(nums, k, multiplier))

    sl = Solution()
    time0 = time.time()

    result = sl.getFinalState(nums, k, multiplier)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
