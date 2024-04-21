import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # 793ms 801ms
        ans, curr =  0, nums[0]
        for num in nums:
            prev, curr = curr, num
            if prev^curr == 0:
                cnt = 0
            cnt += 1
            ans += cnt
        return ans

    def countAlternatingSubarrays2(self, nums: List[int]) -> int:
        # 802ms - 838ms
        ans, size = 1, 1
        for i in range(1, len(nums)):
            size = 1 if nums[i - 1] == nums[i] else size + 1
            ans += size
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

    result = sl.countAlternatingSubarrays(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
