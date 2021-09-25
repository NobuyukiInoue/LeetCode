import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 32ms
        pos = [0]
        for i in range(len(s)):
            for j in pos:
                if s[j:i + 1] in wordDict:
                    pos.append(i + 1)
                    break
        return pos[-1] == len(s)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # 44ms
        check = [True]
        for i in range(1, len(s) + 1):
            check += any(check[j] and s[j:i] in wordDict for j in range(i)),
        return check[-1]

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
    s, wordDict = flds[0], flds[1].split(",")
    print("s = \"{0}\", wordDict = {1}".format(s, wordDict))

    sl = Solution()
    time0 = time.time()

    result = sl.wordBreak(s, wordDict)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
