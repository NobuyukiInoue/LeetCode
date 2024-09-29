import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # 1015ms - 1034ms
        maximumHeight.sort(reverse=True)
        cur, ans = maximumHeight[0], 0
        for num in maximumHeight:
            cur = min(cur, num)
            if cur <= 0:
                return -1
            ans += cur
            cur -= 1
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    maximumHeight = [int(n) for n in flds.split(",")]
    print("maximumHeight = {0}".format(maximumHeight))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumTotalSum(maximumHeight)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
