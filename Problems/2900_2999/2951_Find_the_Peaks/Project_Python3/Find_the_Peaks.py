import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # 52ms - 54ms
        return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] > mountain[i + 1]]

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    mountain = [int(n) for n in flds.split(",")]
    print("mountain = {0}".format(mountain))

    sl = Solution()

    time0 = time.time()

    result = sl.findPeaks(mountain)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
