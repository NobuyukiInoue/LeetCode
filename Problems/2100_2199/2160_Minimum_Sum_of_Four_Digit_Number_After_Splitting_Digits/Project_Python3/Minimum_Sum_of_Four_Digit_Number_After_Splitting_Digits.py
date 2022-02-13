import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumSum(self, num: int) -> int:
        # 34ms
        temp = sorted(str(num))
        return int(temp[0]+temp[2]) + int(temp[1]+temp[3])

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

    result = sl.minimumSum(num)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
