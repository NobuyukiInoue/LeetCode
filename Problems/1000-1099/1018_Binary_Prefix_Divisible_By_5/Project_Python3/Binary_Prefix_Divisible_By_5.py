# coding: utf-8

import os
import sys
import time

class Solution:
#   def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    def prefixesDivBy5(self, A):
        # 96ms
        total = 0
        result = []
        for i in range(0, len(A)):
            total = total*2 +  A[i]
            total = total%5
            if total == 0:
                result.append(True)
            else:
                result.append(False)
        return result

#   def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    def prefixesDivBy5_2(self, A):
        # 300ms
        total = 0
        length = len(A)
        result = [False]*length
        for i in range(length):
            total = total * 2 + A[i]
            if total % 5 == 0:
                result[i] = True
            else:
                result[i] = False
        return result

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
    result = sl.prefixesDivBy5(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]¥n" %(time1 - time0))

if __name__ == "__main__":
    main()
