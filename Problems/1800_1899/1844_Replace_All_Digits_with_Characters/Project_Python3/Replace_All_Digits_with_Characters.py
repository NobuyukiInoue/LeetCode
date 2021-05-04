import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def replaceDigits(self, s):
        # 28ms
        return ''.join(chr(ord(s[i - 1]) + int(s[i])) if i % 2 else s[i] for i in range(len(s)))

    def replaceDigits2(self, s: str) -> str:
        # 32ms
        res = s[0]
        for i in range(1, len(s)):
            ch = ord(s[i]) - 0x30
            if 0 <= ch <= 9:
                res += chr(ord(s[i - 1]) + ch)
            else:
                res += s[i]
        return res

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

    result = sl.replaceDigits(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
