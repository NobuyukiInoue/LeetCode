import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # 973ms - 986ms
        ans, total, dic = 0, 0, set(banned)
        for i in range(1, n + 1):
            if total + i > maxSum:
                break
            if i not in dic:
                total += i
                ans += 1
        return ans

    def maxCount_bad(self, banned: List[int], n: int, maxSum: int) -> int:
        # Time Limit Exceeded. 203/208
        ans, total = 0, 0
        for i in range(1, n + 1):
            if total + i > maxSum:
                break
            if i not in banned:
                total += i
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

    banned = [int(temp) for temp in flds[0].split(",")]
    n, maxSum = int(flds[1]), int(flds[2])
    print("banned = {0}, n = {1:d}, maxSum = {2:d}".format(banned, n, maxSum))

    sl = Solution()
    time0 = time.time()

    result = sl.maxCount(banned, n, maxSum)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
