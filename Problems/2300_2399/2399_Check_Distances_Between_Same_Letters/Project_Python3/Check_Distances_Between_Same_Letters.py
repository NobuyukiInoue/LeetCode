# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # 46ms - 106ms
        for i in range(26):
            ch = chr(ord('a') + i)
            p1 = s.find(ch)
            if p1 == -1:
                continue
            p2 = s.rfind(ch)
            if p2 == -1:
                continue
            if p2 - p1 != distance[i] + 1:
                return False
        return True

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    s = flds[0]
    distance = [int(n) for n in flds[1].split(",")]
    print("s = \"{0}\", k = {1}".format(s, distance))

    sl = Solution()
    time0 = time.time()

    result = sl.checkDistances(s, distance)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
