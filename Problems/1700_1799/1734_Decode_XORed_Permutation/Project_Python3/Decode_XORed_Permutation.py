import functools
import itertools
import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # 825ms - 827ms
        first = functools.reduce(operator.ixor, encoded[::-2] + list(range(len(encoded) + 2)))
        return list(itertools.accumulate([first] + encoded, operator.ixor))

    def decode2(self, encoded: List[int]) -> List[int]:
        # 879ms - 913ms
        n, acc2 = len(encoded), 0
        acc1 = functools.reduce(lambda x, y: x^y,range(1, n + 2))
        for i in range(0,n,2):
            acc2 ^= encoded[i]
        return list(itertools.accumulate(encoded[::-1], operator.xor, initial = acc1^acc2))[::-1]

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    encoded = [int(n) for n in flds.split(",")]
    print("encoded = {0}".format(encoded))

    sl = Solution()

    time0 = time.time()

    result = sl.decode(encoded)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
