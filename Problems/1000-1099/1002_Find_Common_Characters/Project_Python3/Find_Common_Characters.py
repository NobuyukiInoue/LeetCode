import math
import os
import collections
import sys
import time
from functools import reduce

class Solution:
#   def commonChars(self, A: List[str]) -> List[str]:
    def commonChars(self, A):
        # 52ms
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())

    def commonChars2(self, A):
        # 60ms
        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())


def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    A = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.commonChars(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
