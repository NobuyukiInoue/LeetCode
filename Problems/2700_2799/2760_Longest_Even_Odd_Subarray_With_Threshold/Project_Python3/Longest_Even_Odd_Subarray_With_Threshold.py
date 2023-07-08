import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # 338ms - 348ms
        ans, cnt, parity = 0, 0, 0
        for _, num in enumerate(nums):
            if num > threshold:
                cnt = 0
            elif cnt and parity != num%2:
                parity ^= 1
                cnt += 1
            else:
                parity = num%2
                cnt = parity^1
            ans = max(ans, cnt)
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
    threshold = int(flds[1])
    print("nums = {0}, threshold = {1:d}".format(nums, threshold))

    sl = Solution()
    time0 = time.time()

    result = sl.longestAlternatingSubarray(nums, threshold)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
