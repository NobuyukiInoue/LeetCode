import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # 353ms - 369ms
        prev, ans = values[0], 0
        for i in range(1, len(values)):
            val_i = values[i]
            ans = max(ans, val_i - i + prev)
            prev = max(prev, val_i + i)
        return ans

    def maxScoreSightseeingPair_bad(self, values: List[int]) -> int:
        # TimeLimit Exceeded. (45/54)
        n, ans = len(values), 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(ans, values[i] + values[j] + i - j)
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
    values = [int(n) for n in flds.split(",")]
    print("values = {0}".format(values))

    sl = Solution()

    time0 = time.time()

    result = sl.maxScoreSightseeingPair(values)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
