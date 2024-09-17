import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 31ms - 40ms
        d1 = ord(coordinate1[0]) + int(coordinate1[1])
        d2 = ord(coordinate2[0]) + int(coordinate2[1])
        return d1%2 == d2%2

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
    flds = temp.replace("[[","").replace("]]","").replace("\"", "").rstrip().split("],[")
    
    coordinate1, coordinate2 = flds[0], flds[1]
    print("coordinate1 = \"{0}\", coordinate2 = \"{1}\"".format(coordinate1, coordinate2))

    sl = Solution()
    time0 = time.time()

    result = sl.checkTwoChessboards(coordinate1, coordinate2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
