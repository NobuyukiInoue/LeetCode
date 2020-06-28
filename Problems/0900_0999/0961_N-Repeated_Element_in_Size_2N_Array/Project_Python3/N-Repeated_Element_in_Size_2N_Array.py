# coding: utf-8

import os
import sys
import time

class Solution:
#   def repeatedNTimes(self, A: List[int]) -> int:
    def repeatedNTimes2(self, A):
        # 52ms
        return int((sum(A)-sum(set(A))) // (len(A)//2-1))

    def repeatedNTimes(self, A):
        # 40ms
        unique = {}
        for num in A:
            if num in unique:
                return num
            else:
                unique[num] = 0
        return None

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

    A = [int(n) for n in flds.split(",")]
    print("A = {0}".format(A))

    sl = Solution()
    time0 = time.time()
    result = sl.repeatedNTimes(A)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
