# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def findMaximumXOR(self, nums: List[int]) -> int:
    def findMaximumXOR(self, nums):
        # 252ms
        length = len(bin(max(nums))) - 2
        ans = 0
        for i in range(length, -1, -1):
            ans <<= 1
            ans |= 1
            prefixes = {num >> i for num in nums}
            if not any(ans^p in prefixes for p in prefixes):
                ans ^= 1
        return ans

    def findMaximumXOR2(self, nums):
        # 260ms
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

    def findMaximumXOR3(self, nums):
        # 260ms
        return reduce(lambda y,i:y+(any(((y>>i)^p^1)in d for d in[{n>>i for n in nums}]for p in d)<<i),range(32,-1,-1),0)

    def findMaximumXOR4(self, nums):
        # Time Limit Exceeded
        numsLength = len(nums)
        maxXOR = 0
        for i in range(numsLength - 1):
            for j in range(i + 1, numsLength):
                currXOR = nums[i] ^ nums[j]
                if currXOR > maxXOR:
                    maxXOR = currXOR
        return maxXOR

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.findMaximumXOR(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
