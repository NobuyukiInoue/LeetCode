import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # 32ms
        return s1 == s2 or (sum([1 for i in range(len(s1)) if s1[i] != s2[i]]) == 2 and collections.Counter(s1) == collections.Counter(s2))

    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
        # 32ms
        pos = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                pos.append(i)
                if len(pos) > 2:
                    return False
        if len(pos) == 0:
            return True
        if len(pos) == 1:
            return False
        list_s1, list_s2 = list(s1), list(s2)
        list_s2[pos[0]], list_s2[pos[1]] = list_s2[pos[1]], list_s2[pos[0]]
        if list_s1 == list_s2:
            return True
        return False

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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    s1, s2 = flds[0], flds[1]
    print("s1 = {0}, s2 = {1}".format(s1, s2))

    sl = Solution()
    time0 = time.time()

    result = sl.areAlmostEqual(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
