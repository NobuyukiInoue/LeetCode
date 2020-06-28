import math
import os
import sys
import time

class Solution:
#   def numSpecialEquivGroups(self, A: List[str]) -> int:
    def numSpecialEquivGroups(self, A):
        # 36ms
        return len({tuple(sorted(s[0::2]) + sorted(s[1::2])) for s in A})

    def numSpecialEquivGroups2(self, A):
        # 48ms
        uniqueSet = set()
        for word in A:
            tup = [0]*52
            for i in range(len(word)):
                tup[(ord(word[i])-ord('a')) + 26*(i %2)] += 1 
            uniqueSet.add(tuple(tup))
        return len(uniqueSet)

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    A = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("A = {0}".format(A))

    sl = Solution()
    time0 = time.time()
    result = sl.numSpecialEquivGroups(A)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
