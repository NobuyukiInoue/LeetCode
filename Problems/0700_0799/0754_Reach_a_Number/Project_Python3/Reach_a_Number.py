import math
import os
import sys
import time

class Solution:
#    def reachNumber(self, target: int) -> int:
    def reachNumber(self, target):
        target = abs(target)
        n = int(math.ceil(math.sqrt(1 + 8 * target)/2 - 0.5))
        while target % 2 != n * ( n + 1 ) / 2 % 2:
            n += 1
        return n

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    target = int(flds)
    print("target = {0:d}\n".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.reachNumber(target)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
