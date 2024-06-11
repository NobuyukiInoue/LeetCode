import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # 41ms - 43ms
        n -= 1
        rounds, rem = k//n, k%n
        if rounds%2 == 0:
            return rem
        return n - rem

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    n, k = int(flds[0]), int(flds[1])
    print("n = {0:d}, k = {1:d}".format(n, k))

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfChild(n, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
