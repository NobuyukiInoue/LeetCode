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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    A = [int(n) for n in flds.split(",")]
    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.repeatedNTimes(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
