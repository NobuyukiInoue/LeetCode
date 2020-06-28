# coding: utf-8

import os
import sys
import time
import itertools

class Solution:
    # def maxProduct(self, words: List[str]) -> int:
    def maxProduct(self, words):
        # 172ms
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

    # def maxProduct(self, words: List[str]) -> int:
    def maxProduct2(self, words):
        # 976ms
        ws = [(set(w), len(w)) for w in words]
        ret = 0
        for (s1, l1), (s2, l2) in itertools.combinations(ws, 2):
            if not (s1 & s2):
                ret = max(ret, l1 * l2)
        return ret

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    words = flds.split(",")
    print("words {0}".format(words))

    sl = Solution()

    time0 = time.time()

    result = sl.maxProduct(words)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
