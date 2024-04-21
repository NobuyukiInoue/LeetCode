import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def scoreOfString(self, s: str) -> int:
        # 29ms - 30ms
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i - 1]))
        return ans

    def scoreOfString_1liner(self, s: str) -> int:
        # 36ms - 40ms
        return sum(abs(ord(x) - ord(y)) for x, y in itertools.pairwise(s))

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

    result = sl.scoreOfString(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
