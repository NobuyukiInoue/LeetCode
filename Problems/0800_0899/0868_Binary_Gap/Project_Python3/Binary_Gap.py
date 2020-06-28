import math
import os
import sys
import time

class Solution:
#   def binaryGap(self, N: int) -> int:
    def binaryGap(self, N):
        index = [i for i, v in enumerate(bin(N)) if v == '1']
        return max([b - a for a, b in zip(index, index[1:])] or [0])

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    N = int(flds)
    print("N = {0:d}\n".format(N))

    sl = Solution()
    time0 = time.time()

    result = sl.binaryGap(N)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
