import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minCut(self, s: str) -> int:
        # 349ms
        dp = [sys.maxsize] * (len(s) + 1)
        dp[0] = -1
        def isPalindrome(start_idx, end_idx):
            while start_idx >= 0 and end_idx < len(s) and s[start_idx] == s[end_idx]:
                dp[end_idx + 1] = min(dp[end_idx + 1], dp[start_idx] + 1)
                start_idx -= 1
                end_idx += 1
        for i, _ in enumerate(s):
            isPalindrome(i, i)
            isPalindrome(i - 1, i)
        return dp[-1]

    def minCut2(self, s: str) -> int:
        # Time Limit Exceede.
        def partition(s):
            if not s:
                return 0
            m = sys.maxsize
            for i, _ in enumerate(s):
                if s[:i+1] == s[i::-1]:
                    m = min(m, partition(s[i+1:]) + 1)
            return m
        return partition(s) - 1

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
    print("rings = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.minCut(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
