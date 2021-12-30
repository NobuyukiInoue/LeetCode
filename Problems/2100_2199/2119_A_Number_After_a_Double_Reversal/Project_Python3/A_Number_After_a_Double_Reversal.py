import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0            # 32ms
        # return num == 0 or str(num)[-1] != '0'    # 33ms

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
    flds = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.isSameAfterReversals(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
