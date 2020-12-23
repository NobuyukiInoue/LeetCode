import os
import sys
import time
import re
from typing import List, Dict, Tuple

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # 24ms
        def findpat(word):
            tbl = {}
            cnt = 0
            pat = []
            for _, ch in enumerate(word): 
                if ch not in tbl: 
                    cnt += 1 
                    tbl[ch] = cnt
                pat.append(tbl.get(ch))
            return pat
        pattern = findpat(pattern)
        return [word for word in words if findpat(word) == pattern]
 
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
    flds = temp.replace(", ", ",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    words = flds[0].split(",")
    pattern = flds[1]
    print("words = {0}, pattern = {1}".format(words, pattern))

    sl = Solution()
    time0 = time.time()

    result = sl.findAndReplacePattern(words, pattern)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
