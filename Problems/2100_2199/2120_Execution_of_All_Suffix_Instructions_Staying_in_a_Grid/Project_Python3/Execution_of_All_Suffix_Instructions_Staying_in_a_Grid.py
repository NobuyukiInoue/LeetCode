import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # 1130ms - 1131ms
        def helper(n: int, x: int, y: int, s: str) -> int:
            cnt = 0
            for inst in s:
                if inst == "L":
                    x -= 1
                elif inst == "R":
                    x += 1
                elif inst == "U":
                    y -= 1
                elif inst == "D":
                    y += 1
                if x < 0 or y < 0 or x == n or y == n:
                    break
                cnt += 1
            return cnt
        ans = []
        for i, _ in enumerate(s):
            ans.append(helper(n, startPos[1], startPos[0], s[i:]))
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")
    n = int(flds[0])
    startPos = [int(_) for _ in flds[1].split(",")]
    s = flds[2]
    print("n = {0:d}, startPos = {1}, s = \"{2}\"".format(n, startPos, s))

    sl = Solution()
    time0 = time.time()

    result = sl.executeInstructions(n, startPos, s)

    time1 = time.time()

    print("result = {0}\n".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
