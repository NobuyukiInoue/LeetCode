import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # 28ms
        for word in words:
            if s:
                if s.startswith(word):
                    s = s[len(word):]
                else:
                    return False
        return True if not s else False

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
    flds = temp.replace("\"","").replace(", ",",").replace("[[","").replace("]]","").rstrip().split("],[")
    s, words = flds[0], flds[1].split(",")
    print("s = \"{0}\", words = {1}".format(s, words))

    sl = Solution()
    time0 = time.time()

    result = sl.isPrefixString(s, words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
