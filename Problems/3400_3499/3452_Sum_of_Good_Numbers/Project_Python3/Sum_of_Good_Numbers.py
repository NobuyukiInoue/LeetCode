import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        # 0ms
        n, ans = len(nums), 0
        for i in range(n):
            if i + k < n:
                if nums[i] <= nums[i + k]:
                    continue
            if 0 <= i - k:
                if nums[i] <= nums[i - k]:
                    continue
            ans += nums[i]
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    nums, k = [int(num) for num in flds[0].split(",")], int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.sumOfGoodNumbers(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
