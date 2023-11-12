import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 43ms - 52ms
        def helper(n, limit):
            min_v, max_v = max(0, n - limit), min(n, limit)
            return max(0, max_v - min_v + 1)
        ans = 0
        for i in range(min(n, limit) + 1):
            ans += helper(n - i, limit)
        return ans

    def distributeCandies2(self, n: int, limit: int) -> int:
        # 56ms - 57ms
        ans = 0
        for child1 in range(limit + 1):
            remain1 = n - child1
            for child2 in range(limit + 1):
                remain2 = remain1 - child2
                if remain2 <= limit:
                    if remain2 < 0:
                        break
                    ans += 1
        return ans

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

    n, limit = int(flds[0]), int(flds[1])
    print("n = {0:d}, limit = {1:d}".format(n, limit))

    sl = Solution()
    time0 = time.time()

    result = sl.distributeCandies(n, limit)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
