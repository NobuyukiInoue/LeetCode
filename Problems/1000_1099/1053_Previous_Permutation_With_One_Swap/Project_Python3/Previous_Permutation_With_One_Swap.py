# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def prevPermOpt1(self, A: List[int]) -> List[int]:
    def prevPermOpt1(self, A):
        # 248ms
        index, number = -1, 0
        min = sys.maxsize
        lenA = len(A)
        for i in range(lenA -1, 0, -1):
            if A[i] < min:
                min = A[i]
            if min < A[i - 1]:
                number, index = A[i - 1], i
                break
        
        if index == -1:
            return A

        maxTemp, indexer = -1, -1
        for i in range(index, lenA):
            if A[i] > maxTemp and A[i] < number:
                maxTemp, indexer = A[i], i
        
        temper = A[indexer]
        A[indexer] = A[index - 1]
        A[index - 1] = temper

        return A

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    A = [int(num) for num in flds]
    print("A = {0}".format(A))

    time0 = time.time()

    sl = Solution()
    result = sl.prevPermOpt1(A)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
