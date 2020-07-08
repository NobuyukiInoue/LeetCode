import math
import os
import sys
import time

class Solution:
#   def largeGroupPositions(self, S: str) -> List[List[int]]:
    def largeGroupPositions(self, S):
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append((i, j - 1))
            i = j
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
    S = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    print("S = {0}".format(S))

    sl = Solution()
    time0 = time.time()
    result = sl.largeGroupPositions(S)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
