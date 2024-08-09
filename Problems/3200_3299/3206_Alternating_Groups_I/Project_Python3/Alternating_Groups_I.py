import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfAlternatingGroups_1liner(self, colors: List[int]) -> int:
        # 59ms - 63mss
        return sum(colors[i] == colors[i + 2] != colors[i + 1] for i in range(-2, len(colors) - 2))

    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # 46ms - 47ms
        n, ans = len(colors), 0
        for i in range(n):
            if i + 1 < n:
                j = i + 1
            else:
                j = i + 1 - n
            if colors[i] == colors[j]:
                continue
            if i + 2 < n:
                k = i + 2
            else:
                k = i + 2 - n
            if colors[j] == colors[k]:
                continue
            ans += 1
        return ans

    def numberOfAlternatingGroups2(self, colors: List[int]) -> int:
        # 50ms - 54ms
        n = len(colors)
        if n < 3:
            return 0
        ans = 0
        for i in range(n - 2):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                ans += 1
        if colors[0] == colors[n - 2] and colors[0] != colors[n - 1]:
            ans += 1
        if colors[0] != colors[1] and colors[1] == colors[n - 1]:
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    colors = [int(n) for n in flds.split(",")]
    print("colors = {0}".format(colors))

    sl = Solution()

    time0 = time.time()

    result = sl.numberOfAlternatingGroups(colors)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
