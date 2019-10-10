# coding: utf-8

import os
import sys
import time

class Solution:
#    def repeatedStringMatch(self, A: str, B: str) -> int:
    def repeatedStringMatch(self, A, B):
        if not set(B).issubset(set(A)):
            return -1
        elif B in A:
            return 1
        
        max_times = len(B)//len(A) + 2
        for i in range(len(B)//len(A),max_times+1):
            if B in A*i:
                return i   
        return -1

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")
    A = flds[0]
    B = flds[1]
    print("A = %s" %A)
    print("B = %s" %B)

    time0 = time.time()

    sl = Solution()
    result = sl.repeatedStringMatch(A, B)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
