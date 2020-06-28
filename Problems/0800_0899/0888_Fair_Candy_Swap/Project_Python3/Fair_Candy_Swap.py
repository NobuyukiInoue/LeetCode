# coding: utf-8

import os
import sys
import time

class Solution:
#   def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    def fairCandySwap(self, A, B):
        dif = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    data = flds[0].split(",")
    A = [0]*len(data)
    for i in range(len(data)):
        A[i] = int(data[i])

    data = flds[1].split(",")
    B = [0]*len(data)
    for i in range(len(data)):
        B[i] = int(data[i])
    
    print("A = {0}, B = {1}".format(A, B))

    sl = Solution()
    time0 = time.time()
    result = sl.fairCandySwap(A, B)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
