import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # 245ms - 248ms
        res, cnt1, cnt2 = 0, 0, 0
        for ch in text:
            if ch == pattern[1]:
                res += cnt1
                cnt2 += 1
            if ch == pattern[0]:
                cnt1 += 1
        return res + max(cnt1, cnt2)

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    text, pattern = flds[0], flds[1]
    print("text = \"{0}\", pattern = \"{1}\"".format(text, pattern))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumSubsequenceCount(text, pattern)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
