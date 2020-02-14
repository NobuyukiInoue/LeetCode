# coding: utf-8

import os
import sys
import time

class Solution:
#   def canThreePartsEqualSum(self, A: List[int]) -> bool:
    def canThreePartsEqualSum(self, A):
        total = sum(A)
        if total % 3 != 0:
            return False
        sub_total, count, hit = 0, 0, total // 3
        for i in range(len(A)):
            sub_total += A[i]
            if sub_total == hit:
                sub_total = 0
                count += 1
        if count == 3:
            return True
        else:
            return False

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

    A = [int(val) for val in flds]
    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.canThreePartsEqualSum(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]¥n" %(time1 - time0))

if __name__ == "__main__":
    main()
