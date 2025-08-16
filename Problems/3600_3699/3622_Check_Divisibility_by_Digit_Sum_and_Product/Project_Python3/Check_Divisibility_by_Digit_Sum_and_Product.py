import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # 0ms
        v_prd, v_sum, temp_n = 1, 0, n
        while temp_n > 0:
            m = temp_n%10
            v_prd, v_sum = m*v_prd, m + v_sum
            temp_n //= 10
        return n %(v_prd + v_sum) == 0

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

    result = sl.checkDivisibility(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
