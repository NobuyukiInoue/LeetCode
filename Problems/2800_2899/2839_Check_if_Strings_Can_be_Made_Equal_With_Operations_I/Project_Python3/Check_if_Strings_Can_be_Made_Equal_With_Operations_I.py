import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # 29ms - 34ms
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

    def canBeEqual1(self, s1: str, s2: str) -> bool:
        # 40ms - 47ms
        if s1 == s2:
            return True
        l_s1 = list(s1)
        for i in range(2):
            if l_s1[i] == s2[i + 2]:
                l_s1[i], l_s1[i + 2] = l_s1[i + 2], l_s1[i]
            if "".join(l_s1) == s2:
                return True
        return False

    def canBeEqual2(self, s1: str, s2: str) -> bool:
        # 44ms - 45ms
        if s1 == s2:
            return True
        l_s1 = list(s1)
        for i, j in ([0, 2], [1, 3]):
            l_s1[i], l_s1[j] = l_s1[j], l_s1[i]
            if "".join(l_s1) == s2:
                return True
        l_s1 = list(s1)
        for i, j in ([1, 3], [0, 2]):
            l_s1[i], l_s1[j] = l_s1[j], l_s1[i]
            if "".join(l_s1) == s2:
                return True
        return False

    def canBeEqual2(self, s1: str, s2: str) -> bool:
        # 37ms - 43ms
        if s1 == s2:
            return True
        l_s1 = list(s1)
        l_s1[0], l_s1[2] = l_s1[2], l_s1[0]
        if "".join(l_s1) == s2:
            return True
        l_s1[1], l_s1[3] = l_s1[3], l_s1[1]
        if "".join(l_s1) == s2:
            return True
        l_s1 = list(s1)
        l_s1[1], l_s1[3] = l_s1[3], l_s1[1]
        if "".join(l_s1) == s2:
            return True
        l_s1[0], l_s1[2] = l_s1[2], l_s1[0]
        if "".join(l_s1) == s2:
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    s1, s2  = flds[0], flds[1]
    print("s1 = \"{0}\", s2 = \"{1}\"".format(s1, s2))

    sl = Solution()
    time0 = time.time()

    result = sl.canBeEqual(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
