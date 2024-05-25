import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # 35ms - 38ms
        ans = 0
        for i, _ in enumerate(s):
            ans += abs(s.index(s[i]) - t.index(s[i]))
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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    
    s, t = flds[0], flds[1]
    print("s = \"{0}\", t = \"{1}\"".format(s, t))

    sl = Solution()
    time0 = time.time()

    result = sl.findPermutationDifference(s, t)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
