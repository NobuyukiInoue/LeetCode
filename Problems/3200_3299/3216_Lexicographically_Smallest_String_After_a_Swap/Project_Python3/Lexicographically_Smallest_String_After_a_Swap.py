import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getSmallestString(self, s: str) -> str:
        # 28ms - 41ms
        for i in range(len(s) - 1):
            m1, m2 = int(s[i])%2, int(s[i + 1])%2
            if m1 == m2 and s[i] > s[i + 1]:
                return s[:i] + s[i + 1] + s[i] + s[i + 2:]
        return s

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
    s = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("s = \"{0}\"".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.getSmallestString(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
