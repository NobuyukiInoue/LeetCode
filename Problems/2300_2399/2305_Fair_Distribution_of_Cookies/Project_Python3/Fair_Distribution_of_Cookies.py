# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 50ms - 78ms
        n = len(cookies)
        self.children = [0]*k
        self.ans = sys.maxsize
        def helper(i: int, current_max: int) -> None:
            if i == n:
                self.ans = min(self.ans, current_max)
                return
            if current_max >= self.ans:
                return
            for j in range(k):
                self.children[j] += cookies[i]
                helper(i + 1, max(current_max, self.children[j]))
                self.children[j] -= cookies[i]
        helper(0, 0)
        return self.ans

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    cookies = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("cookies = {0}, k = {1:d}".format(cookies, k))

    sl = Solution()
    time0 = time.time()

    result = sl.distributeCookies(cookies, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
