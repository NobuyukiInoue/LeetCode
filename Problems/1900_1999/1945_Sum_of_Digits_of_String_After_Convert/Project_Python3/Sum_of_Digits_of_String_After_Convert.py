import functools
import os
import sys
import string
import time
from typing import List, Dict, Tuple

class Solution:
    def getLucky1(self, s: str, k: int) -> int:
        return int(functools.reduce(lambda s,_: str(sum(map(int, s))), range(k), ''.join(map(str, map(('_' + string.ascii_lowercase).index, s)))))

    def getLucky2(self, s: str, k: int) -> int:
        # 52ms
        s = ''.join(map(str, map(('_' + string.ascii_lowercase).index, s)))
        for _ in range(k):
            s = str(sum(map(int, s)))
        return int(s)

    def getLucky(self, s: str, k: int) -> int:
        # 28ms
        workStr = ""
        for ch in s:
            workStr += str(ord(ch) - 96)
        while k != 0:
            ans = 0
            for ch in workStr:
                ans += int(ch)
            workStr = str(ans)
            k -= 1
        return ans

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, k = flds[0], int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.getLucky(s, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
