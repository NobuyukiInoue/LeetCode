import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # 652ms - 685ms
        res, pre = "", 0
        for pos in spaces:
            res += s[pre:pos] + " "
            pre = pos
        res += s[pre:]
        return res

    def addSpaces2(self, s: str, spaces: List[int]) -> str:
        # 830ms - 844ms
        ans, j = [], 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(c)
        return ''.join(ans)

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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s = flds[0]
    spaces = [int(num) for num in flds[1].split(",")]
    print("s = \"{0}\", spaces = {1}".format(s, spaces))

    sl = Solution()
    time0 = time.time()

    result = sl.addSpaces(s, spaces)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
