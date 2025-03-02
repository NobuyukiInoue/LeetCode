import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def smallestNumber1(self, n: int) -> int:
        # 0ms
        cur = 1
        while cur - 1 < n:
            cur <<= 1
        return cur - 1

    def smallestNumber(self, n: int) -> int:
        # 0ms
        return pow(2, n.bit_length()) - 1
    
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.smallestNumber(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
