# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def evenOddBit_1liner(self, n: int) -> List[int]:
        # 35ms
        return [(n & 0b10101010101).bit_count(), (n & 0b01010101010).bit_count()]
    
    def evenOddBit(self, n: int) -> List[int]:
        # 36ms - 37ms
        odd = False
        ans = [0, 0]
        while n > 0:
            if odd == False:
                if n & 1 > 0:
                    ans[0] += 1
                odd = True
            else :
                if n & 1 > 0:
                    ans[1] += 1
                odd = False
            n //= 2
        return ans

    def evenOddBit2(self, n: int) -> List[int]:
        # 37ms
        s = bin(n)[2:][::-1]
        even, odd = 0, 0
        for i, _ in enumerate(s):
            if i%2 == 1 and s[i] =='1':
                odd += 1
            if i%2 == 0 and s[i] =='1':
                even += 1
        return [even, odd]

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
    fld = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(fld)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.evenOddBit(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
