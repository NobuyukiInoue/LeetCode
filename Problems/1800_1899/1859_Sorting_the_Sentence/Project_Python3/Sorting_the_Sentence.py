import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sortSentence(self, s: str) -> str:
        # 20ms
        words = s.split(" ")
        flds = [None]*len(words)
        for word in words:
            flds[int(word[-1]) - 1] = word[:-1]
        return " ".join(flds)

    def sortSentence2(self, s: str) -> str:
        # 32ms
        return " ".join([i[:-1] for i in sorted(s.split(), key=lambda x: x[-1])])

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

    result = sl.sortSentence(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
