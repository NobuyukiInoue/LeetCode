# coding: utf-8

import os
import sys
import time

class Solution:
#   def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    def addToArrayForm(self, A, K):
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
        return [int(i) for i in str(K)] + A if K else A

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    A = [int(n) for n in flds[0].split(",")]
    K = int(flds[1])
    print("A = %s, K = %d" %(A, K))

    time0 = time.time()

    sl = Solution()
    result = sl.addToArrayForm(A, K)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
