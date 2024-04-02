import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # 32ms - 37ms
        ans, prefix, prev = 0, 0, 0
        for i, ch in enumerate(s):
            if ch == '1':
                ans = max(prev, i - prefix)
                prefix += 1
                if ans:
                    prev = ans + 1
        return ans

    def secondsToRemoveOccurrences2(self, s: str) -> int:
        # 100ms - 103ms
        cnt = 0
        while "01" in s:
            s = s.replace("01", "10", -1)
            cnt += 1
        return cnt

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

    result = sl.secondsToRemoveOccurrences(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
