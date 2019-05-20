# coding: utf-8

import os
import sys
import time

class Solution:
#   def sortArrayByParity(self, A: List[int]) -> List[int]:
    def sortArrayByParity(self, A):
        return([i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0])

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    A = [int(val) for val in flds]
    
    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.sortArrayByParity(A)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
