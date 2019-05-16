# coding: utf-8

import bisect
import os
import sys
import time

class Solution:
#   def maxWidthRamp(self, A: List[int]) -> int:
    def maxWidthRamp(self, A):
        # 168ms
        stack = []
        res = 0
        for i in range(len(A))[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append([A[i], i])
            else:
                j = stack[bisect.bisect(stack, [A[i], i])][1]
                res = max(res, j - i)
        return res

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
    result = sl.maxWidthRamp(A)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
