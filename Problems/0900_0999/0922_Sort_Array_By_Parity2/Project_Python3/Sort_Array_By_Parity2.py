# coding: utf-8

import os
import sys
import time

class Solution:
#   def sortArrayByParityII(self, A: List[int]) -> List[int]:
    def sortArrayByParityII(self, A):
        # 148ms
        odd = len(A) - 1
        even = len(A) - 2
        while even >= 0 and odd >= 0:
            if A[0] % 2 == 1:
                A[0], A[odd] = A[odd], A[0]
                odd -= 2
            else:
                A[0], A[even] = A[even], A[0]
                even -= 2
        return A

    def sortArrayByParityII_2(self, A):
        # 144ms
        even, odd = [a for a in A if not a % 2], [a for a in A if a % 2]
        return [even.pop() if not i % 2 else odd.pop() for i in range(len(A))]

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

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

    A = str_to_int_array(flds)

    print("A = %s" %A)

    time0 = time.time()

    sl = Solution()
    result = sl.sortArrayByParityII(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
