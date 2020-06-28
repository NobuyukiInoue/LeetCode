# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def rebarcodesangeBarcodes(self, barcodes: List[int]) -> List[int]:
    def rebarcodesangeBarcodes(self, barcodes):
        # 440ms
        i, n = 0, len(barcodes)
        res = [0] * n
        for k, v in collections.Counter(barcodes).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    barcodes = [int(num) for num in flds]
    print("barcodes = {0}".format(barcodes))

    sl = Solution()
    time0 = time.time()
    result = sl.rebarcodesangeBarcodes(barcodes)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
