import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # 66ms - 71ms
        nums = enumerate(itertools.zip_longest(*map(
                   lambda x: bin(x)[-1:1:-1],nums),fillvalue = '0'))
        return sum((1<<i)for i,arr in nums if arr.count('1') >= k)

    def findKOr2(self, nums: List[int], k: int) -> int:
        # 85ms - 104ms
        ans = 0
        for i in range(32):
            count = sum((num >> i) & 1 for num in nums)
            if count >= k:
                ans |= (1 << i)
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.findKOr(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
