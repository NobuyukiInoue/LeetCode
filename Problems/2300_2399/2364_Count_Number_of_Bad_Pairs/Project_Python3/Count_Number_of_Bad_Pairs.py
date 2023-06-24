import collections
import itertools
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # 701ms - 727ms
        count_dict = collections.defaultdict(int)
        ans = 0
        for i, _ in enumerate(nums):
            prev = count_dict[i - nums[i]]
            ans += (i - prev)
            count_dict[i - nums[i]] = prev + 1
        return ans

    def countBadPairs2(self, nums: List[int]) -> int:
        # 698ms - 722ms
        nums_len = len(nums)
        count_dict = collections.defaultdict(int)
        for i in range(nums_len):
            nums[i] -= i
            count_dict[nums[i]] += 1
        count = 0
        for key in count_dict:
            count += math.comb(count_dict[key], 2)
        return math.comb(nums_len, 2) - count

    def countBadPairs_bad(self, nums: List[int]) -> int:
        # Time Limite Exceeded. 42/65
        patterns = list(itertools.combinations(range(len(nums)), 2))
        ans = 0
        for (i, j) in patterns:
            if j - i != nums[j] - nums[i]:
                ans += 1
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

    result = sl.countBadPairs(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
