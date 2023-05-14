import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 35ms - 50ms
        s = s.rstrip()
        i = len(s) - 1
        while s[i] != " " and i >= 0:
            i -= 1
        return (len(s) - 1) - i

    def lengthOfLastWord_2liner(self, s: str) -> int:
        # 44ms - 48ms
        arr = s.rstrip().split(" ")
        return len(arr[-1])

    def lengthOfLastWord_1liner(self, s: str) -> int:
        # 47ms - 52ms
        return len(s.rstrip().split(" ")[-1])

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
    print("s = \"{0}\"".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.lengthOfLastWord(s)

    time1 = time.time()
    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
