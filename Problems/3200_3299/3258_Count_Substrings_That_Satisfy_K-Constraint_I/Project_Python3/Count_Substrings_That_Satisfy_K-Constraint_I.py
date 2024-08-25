import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # 54ms - 55ms
        ans, n = 0, len(s)
        for i in range(n):
            count0, count1 = 0, 0
            for j in range(i, n):
                if s[j] == "0":
                    count0 += 1
                else:
                    count1 += 1
                if count0 <= k or count1 <= k:
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
    flds = temp.replace("[[","").replace("]]","").rstrip().split("],[")
    
    s, k = flds[0].replace("\"", ""), int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.countKConstraintSubstrings(s, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
