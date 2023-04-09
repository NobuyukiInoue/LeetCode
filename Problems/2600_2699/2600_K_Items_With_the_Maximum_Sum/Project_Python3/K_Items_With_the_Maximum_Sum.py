import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # 37ms - 38ms
        return min(k, numOnes) - max(0, k - numZeros - numOnes)

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

    numOnes, numZeros, numNegOnes, k = int(flds[0]), int(flds[1]), int(flds[2]), int(flds[3])
    print("numOnes = {0:d}, numZeros = {1:d}, numNegOnes = {2:d}, k = {3:d}".format(numOnes, numZeros, numNegOnes, k))

    sl = Solution()
    time0 = time.time()

    result = sl.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
