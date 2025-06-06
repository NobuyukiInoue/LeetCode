import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # 43ms - 48ms
        left, right = 0, 0
        for i, num  in enumerate(nums):
            left += num
            if num == 0:
                index = i
                break
        for i, num  in enumerate(nums[index:]):
            right += num
        count = 0
        for i, num  in enumerate(nums[index:]):
            left += num
            right -= num 
            if num != 0:
                continue
            if left == right:
                count += 2
            elif left - 1 == right or left + 1 == right:
                count += 1
        return count
    
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

    result = sl.countValidSelections(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
