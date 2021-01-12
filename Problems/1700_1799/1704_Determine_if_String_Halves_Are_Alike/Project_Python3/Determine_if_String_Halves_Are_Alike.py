import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 24ms
        vowls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s) // 2
        a, b = collections.Counter(s[:mid]), collections.Counter(s[mid:])
        return sum(a[v] for v in vowls) == sum(b[v] for v in vowls)

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.halvesAreAlike(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
