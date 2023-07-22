import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # 881ms - 913ms
        nums.sort()
        ans, start = 1, nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - start
            if diff > k:
                ans += 1
                start = nums[i]
        return ans

    def partitionArray2(self, nums: List[int], k: int) -> int:
        # 921ms - 951ms
        nums.sort()
        n, l, r, cnt = len(nums), 0, 0, 0
        while r < n:
            if nums[r] - nums[l] <= k:
                r += 1
            else:
                l = r
                cnt += 1
        return cnt + 1
    
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

    result = sl.partitionArray(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
