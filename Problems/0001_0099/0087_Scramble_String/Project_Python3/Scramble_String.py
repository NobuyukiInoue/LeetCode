import os
import sys
import time
import re

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 36ms
        m, n = len(s1), len(s2)
        if m != n or sorted(s1) != sorted(s2):
            return False
        if m < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
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
    flds = temp.replace(", ", ",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    s1, s2 = flds[0], flds[1]
    print("s1 = {0}, s2 = {1}".format(s1, s2))

    sl = Solution()
    time0 = time.time()

    result = sl.isScramble(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
