import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        # 47ms - 54ms
        ans = 0
        for num in nums:
            m, l = 0, 0
            while num > 0:
                m = max(m, num%10)
                num //= 10
                l += 1
            while l > 0:
                ans += m
                m *= 10
                l -= 1
        return ans

    def sumOfEncryptedInt2(self, nums: List[int]) -> int:
        # 48ms - 53ms
        def encrypt(x):
            cur = str(x)
            value = max(cur)
            return int(value*len(cur))
        cur_sum = 0
        for i in nums:
            cur_sum += encrypt(i)
        return cur_sum

    def sumOfEncryptedInt3(self, nums: List[int]) -> int:
        # 49ms - 59ms
        def en(num):
            min_val = max([int(i) for i in str(num)])
            dig = int(str(min_val)*len(str(num)))
            return dig
        return sum(en(num) for num in nums)


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

    result = sl.sumOfEncryptedInt(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
