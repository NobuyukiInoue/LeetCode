import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        # 0ms - 4ms
        count = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1] and count == k:
                return True
            if s[i] != s[i - 1]:
                count = 0
            count += 1
        return count == k

    def hasSpecialSubstring_1liner(self, s: str, k: int) -> bool:
        return any(len(list(grp)) == k for _, grp in itertools.groupby(s))
    
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    s, k = flds[0], int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.hasSpecialSubstring(s, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
