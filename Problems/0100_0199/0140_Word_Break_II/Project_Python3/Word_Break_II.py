import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 37ms - 62ms
        n = len(s)
        def dfs(i):
            if i == n:
                return [""]
            ans = []
            for k in range(i, n):
                left = s[i:k + 1]
                if left in wordDict:
                    for right in dfs(k + 1):
                        if right:
                            ans.append(left + " " + right)
                        else:
                            ans.append(left + right)
            return ans
        return dfs(0)

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
