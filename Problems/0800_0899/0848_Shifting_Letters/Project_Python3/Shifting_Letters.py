import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # 168ms
        acum = 0
        s2 = list(s)
        for i in range(len(s2) - 1, -1, -1):
            acum += shifts[i]
            s2[i] = chr(97 + (ord(s2[i])+acum-97) % 26)
        return "".join(s2)

    def shiftingLetters2(self, s: str, shifts: List[int]) -> str:
        # 184ms
        sm, res = sum(shift % 26 for shift in shifts) % 26, ""
        for i, ch in enumerate(shifts):
            move, sm = ord(s[i]) + sm % 26, sm - ch
            res += chr(move > 122 and move - 26 or move)
        return res

    def shiftingLetters_work(self, s: str, shifts: List[int]) -> str:
        # 192ms
        total = sum(shifts)
        adds = [0]*len(shifts)
        n = len(shifts)
        adds[0] = total
        for i in range(1, n):
            adds[i] = adds[i - 1] - shifts[i - 1]
        res = [0]*n
        ans = [""]*n
        for i in range(n):
            res[i] = ord(s[i]) + adds[i] % 26
            if res[i] > ord('z'):
                res[i] -= 26
            ans[i] = chr(res[i])
        return "".join(ans)

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
    s = flds[0]
    shifts = [int(n) for n in flds[1].split(",")]

    print("s = {0}".format(s))
    print("shifts = {0}".format(shifts))

    sl = Solution()
    time0 = time.time()

    result = sl.shiftingLetters(s, shifts)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
