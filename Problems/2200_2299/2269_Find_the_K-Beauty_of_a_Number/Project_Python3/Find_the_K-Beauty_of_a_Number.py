# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # 37ms - 44ms
        str_num = str(num)
        ans = 0
        for i in range(0, len(str_num) - k + 1):
            temp = int(str_num[i:i+k])
            if temp != 0 and num % temp == 0:
                ans += 1
        return ans

    def divisorSubstrings_2liner(self, num: int, k: int) -> int:
        # 45ms - 60ms
        str_num = str(num)      
        return sum(1 for i in range(len(str_num)-k+1) if int(str_num[i:i+k]) and num % int(str_num[i:i+k]) == 0)

    def divisorSubstrings2(self, num: int, k: int) -> int:
        # 37ms - 61ms
        l, r = 0, k
        num = str(num)
        count = 0
        while r <= len(num):            
            n = int(num[l: r])
            if not n:
                l += 1
                r += 1
                continue
            if int(num) % n == 0:
                count += 1   
            l += 1
            r += 1
        return count

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
    num, k = nums[0], nums[1]
    print("num = {0:d}, k = {1:d}".format(num, k))

    sl = Solution()

    time0 = time.time()

    result = sl.divisorSubstrings(num, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
