import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 26ms -35ms
        return n - abs(n - 1 - time % (n * 2 - 2))

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

    n = int(flds[0])
    v_time = int(flds[1])
    print("n = {0:d}, time = {1:d}".format(n, v_time))

    sl = Solution()
    time0 = time.time()

    result = sl.passThePillow(n, v_time)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
