import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # 28ms
        col1, col2 = ord(s[0]), ord(s[3])
        row1, row2 = int(s[1]), int(s[4])
        return [chr(col) + str(row) for col in range(col1, col2 + 1) for row in range(row1, row2 + 1)]

    def cellsInRange_work(self, s: str) -> List[str]:
        # 44ms
        ord_A = ord('A')
        flds = s.split(":")
        row1, col1 = int(flds[0][1]) - 1, ord(flds[0][0]) - ord_A
        row2, col2 = int(flds[1][1]) - 1, ord(flds[1][0]) - ord_A
        ans = []
        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                ans.append(chr(col + ord_A) + str(row + 1))
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
    s = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.cellsInRange(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
