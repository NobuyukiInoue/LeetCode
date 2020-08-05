# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def restoreString(self, s: str, indices: List[int]) -> str:
    def restoreString(self, s, indices):
        # 44ms
        res = [None]*len(s)
        for i, c in enumerate(s):
            res[indices[i]] = c
        return "".join(res)

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, indices = flds[0], [int(n) for n in flds[1].split(",")]
    print("s = {0}, indices = {1}".format(s, indices))

    sl = Solution()
    time0 = time.time()

    result = sl.restoreString(s, indices)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
