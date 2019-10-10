# coding: utf-8

import os
import sys
import time

class Solution:
#   def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    def flipAndInvertImage(self, A):
        return [[1 - i for i in row[::-1]] for row in A]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    A = [0]*len(flds)
    for i in range(len(flds)):
        pt = flds[i].split(",")
        A[i] = [0]*len(pt)
        for j in range(len(pt)):
            A[i][j] = int(pt[j])
    
    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.flipAndInvertImage(A)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
