import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getSneakyNumbers1(self, nums: List[int]) -> List[int]:
        # 45ms - 62ms
        cnts = collections.Counter(nums)
        return [k for k, v in cnts.items() if v > 1]

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # 37ms - 58ms
        cnts = collections.defaultdict(int)
        ans = []
        for num in nums:
            cnts[num] += 1
            if cnts[num] == 2:
                ans.append(num)
        return ans

    def getSneakyNumbers3(self, nums: List[int]) -> List[int]:
        # 45ms - 46ms
        cnts = set()
        ans = []
        for num in nums:
            if num in cnts:
                ans.append(num)
            else:
                cnts.add(num)
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.getSneakyNumbers(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
