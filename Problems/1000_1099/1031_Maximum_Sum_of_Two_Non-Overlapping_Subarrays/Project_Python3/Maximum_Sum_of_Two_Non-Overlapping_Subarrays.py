# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # 52ms - 63ms
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        f, s = firstLen, secondLen
        maxf, maxs, maxt = nums[f - 1], nums[s - 1], nums[f + s - 1]
        for i in range(f+s, len(nums)):
            maxf = max(maxf, nums[i - s] - nums[i - s - f])
            maxs = max(maxs, nums[i - f] - nums[i - f - s])
            maxt = max(maxt, max(maxf + nums[i] - nums[i - s], maxs + nums[i] - nums[i - f]))
        return maxt

    def maxSumTwoNoOverlap2(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # 80ms - 81ms
        def trail(nums: List[int], firstLen: int, secondLen: int) -> int:
            sa = ba = sum(nums[:firstLen])
            sb = sum(nums[firstLen : secondLen + firstLen])
            best = ba + sb
            for i in range(secondLen + firstLen, len(nums)):
                sa += nums[i - secondLen] - nums[i - secondLen - firstLen]
                sb += nums[i] - nums[i - secondLen]
                ba = max(ba, sa)
                best = max( best, ba + sb)
            return best
        maxLMsum = trail(nums, firstLen, secondLen)
        maxMLsum = trail(nums, secondLen, firstLen)
        return max(maxLMsum, maxMLsum)

    def maxSumTwoNoOverlap3(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # 41ms - 68ms
        length = len(nums)
        dp, mysum = [0]*length, sum(nums[-secondLen:])
        mymax, dp[-secondLen] = mysum, mysum
        for i in range(length - secondLen - 1, -1, -1):
            mysum += nums[i] - nums[i + secondLen]
            mymax = max(mymax,mysum)
            dp[i] = mymax
        mysum = sum(nums[:firstLen])
        mymax, result = mysum,mysum + dp[firstLen]
        for i in range(firstLen, length - secondLen):
            mysum += nums[i] - nums[i - firstLen]
            mymax = max(mymax, mysum)
            result = max(result,mymax+dp[i+1])
        dp, mysum = [0]*length, sum(nums[-firstLen:])
        mymax, dp[-firstLen] = mysum, mysum
        for i in range(length - firstLen - 1, -1, -1):
            mysum += nums[i] - nums[i + firstLen]
            mymax = max(mymax, mysum)
            dp[i] = mymax
        mysum = sum(nums[:secondLen])
        mymax,result = mysum,max(result, mysum + dp[secondLen])
        for i in range(secondLen, length - firstLen):
            mysum += nums[i] - nums[i - secondLen]
            mymax = max(mymax, mysum)
            result = max(result, mymax + dp[i+1])
        return result
 
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    firstLen, secondLen = int(flds[1]), int(flds[2])
    print("nums = {0}, firstLen = {1:d}, secondLen = {2:d}".format(nums, firstLen, secondLen))

    sl = Solution()
    time0 = time.time()

    result = sl.maxSumTwoNoOverlap(nums, firstLen, secondLen)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
