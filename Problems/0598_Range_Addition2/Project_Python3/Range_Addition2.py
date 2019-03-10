# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    def maxCount(self, m: int, n: int, ops):
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)

    def maxCount_work(self, m: int, n: int, ops):
        if len(ops) <= 1:
            if len(ops[0]) == 0:
                return m * n
        data = [[0 for j in range(n)] for i in range(m)]
        max, count = 0, m*n
        for cur_ops in ops:
            for i in range(cur_ops[0]):
                for j in range(cur_ops[1]):
                    data[i][j] += 1
                    if data[i][j] > max:
                        max = data[i][j]
                        count = 1
                    elif data[i][j] == max:
                        count += 1
        return count

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
    flds = temp.replace("\"","").replace(" ","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")
    m_and_n = flds[0].split("],[")
    m = int(m_and_n[0])
    n = int(m_and_n[1])
    print("m = %d, n = %d" %(m, n))

    if len(flds[1]) == 0:
        ops = []
    else:
        nums = flds[1].split("],[")
        data0 = nums[0].split(",")
        ops = [[0 for j in range(len(data0))] for i in range(len(nums))]

        for i in range(len(nums)):
            line = nums[i].split(",")
            for j in range(len(line)):
                ops[i][j] = int(line[j])
            print("ops[%d] = %s" %(i, ops[i]))
 
    print("ops[] = %s" %ops)

    time0 = time.time()

    sl = Solution()
    result = sl.maxCount(m, n, ops)

    time1 = time.time()

    print()
    print("result = %d" %result)
    for i in range(len(ops)):
        print("ops[%d] = %s" %(i, ops[i]))

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
