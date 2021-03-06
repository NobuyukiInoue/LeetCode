import math
import os
import sys
import time

class Solution:
#    def rotateString(self, A: str, B: str) -> bool:
    def rotateString2(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A

    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        for i in range (1, len(A)):
            temp = A[i:] + A[0:i]
            if temp == B:
                return True

        return False

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
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    A = words[0]
    B = words[1]
    print("A = {0}, B = {1}".format(A, B))

    sl = Solution()
    time0 = time.time()
    result = sl.rotateString(A, B)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
