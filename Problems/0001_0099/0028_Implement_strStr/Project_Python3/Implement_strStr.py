import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 31ms - 38ms
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        # 32ms - 40ms
        for i, char in enumerate(haystack):
            if char == needle[0] and (i + len(needle) - 1) < len(haystack) and haystack[i:i + len(needle)] == needle:
                return i
        return -1

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    haystack = flds[0]
    needle = flds[1]
    print("haystack = {0}, needle = {1}".format(haystack, needle))

    sl = Solution()
    time0 = time.time()

    result = sl.strStr(haystack, needle)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
