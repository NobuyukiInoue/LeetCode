import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 28ms
        dp = [1]*5
        for _ in range(n-1):
            dp = itertools.accumulate(dp)
        return sum(dp)

    def countVowelStrings_twoloop(self, n: int) -> int:
        # 33ms - 46ms
        dp = [1 for i in range(5)]
        for _ in range(2, n + 1):
            for j in range(1, 5):
                dp[j] = dp[j] + dp[j - 1]
        return sum(dp)

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
    flds = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.countVowelStrings(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
