import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # 24ms
        n, sLength = 0, len(s)
        for i in range(len(s)):
            if s[i] == ' ':
                n += 1
            if n == k:
                sLength = i
                break
        return s[:sLength]

    def truncateSentence2(self, s: str, k: int) -> str:
        # 32ms
        return " ".join(s.split(" ")[:k])

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, k = flds[0], int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.truncateSentence(s, k)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
