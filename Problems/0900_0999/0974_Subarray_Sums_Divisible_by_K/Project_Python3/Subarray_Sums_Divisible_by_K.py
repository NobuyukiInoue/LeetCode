import collections
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 208ms - 222ms
        mod = [0]*k
        mod[0] = 1
        running_mod = 0
        for num in nums:
            running_mod = (num + running_mod)%k
            mod[running_mod] += 1
        return sum([n*(n - 1)//2 for n in mod])

    def subarraysDivByK_1liner(self, nums: List[int], k: int) -> int:
        # 229ms - 230ms
        return sum(r*(r - 1)//2 for _, r in collections.Counter(map(lambda x: x%k, itertools.accumulate([0] + nums))).items())

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

    result = sl.subarraysDivByK(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
