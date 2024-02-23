import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # 52ms - 72ms
        ans = [words[0]]
        for i in range(1, len(words)):
            if groups[i] == groups[i - 1]:
                continue
            ans.append(words[i])
        return  ans

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
    flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").rstrip().split("],[")
    words, groups = flds[0].split(","), [int(_) for _ in flds[1].split(",")]
    print("words = {0}, groups = {1}".format(words, groups))

    sl = Solution()
    time0 = time.time()

    result = sl.getLongestSubsequence(words, groups)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
