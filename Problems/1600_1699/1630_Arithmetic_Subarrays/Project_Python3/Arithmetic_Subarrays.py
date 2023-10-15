import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 148ms - 152ms
        def checkDiff(temp: List[int]) -> bool:
            diff = temp[1] - temp[0]
            for i in range(2, len(temp)):
                if temp[i] - temp[i - 1] != diff:
                    return False
            return True
        ans = []
        for x, y in zip(l, r):
            temp = nums[x : y + 1]
            temp.sort()
            ans.append(checkDiff(temp))
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
    
    nums = [int(_) for _ in flds[0].split(",")]
    l = [int(_) for _ in flds[1].split(",")]
    r = [int(_) for _ in flds[2].split(",")]
    print("nums = {0}, l = {1}, r = {2}".format(nums, l, r))

    sl = Solution()
    time0 = time.time()

    result = sl.checkArithmeticSubarrays(nums, l, r)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
