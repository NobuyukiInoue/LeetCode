# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    def imageSmoother(self, M):
        RES = copy.deepcopy(M)
        TEMP = [[0 for j in range(len(M[0]) + 2)] for i in range(len(M) + 2)]

        for i in range(len(M) * len(M[0])):
            TEMP[i // len(M[0]) + 1][i % len(M[0]) + 1] = M[i // len(M[0])][i % len(M[0])]

        for i in range(len(M) * len(M[0])):
            row   = i // len(M[0])
            col   = i % len(M[0])
            count = 9
            sum = TEMP[row + 1][col + 1] + \
                    TEMP[row + 0][col + 0] + \
                    TEMP[row + 0][col + 1] + \
                    TEMP[row + 0][col + 2] + \
                    TEMP[row + 1][col + 0] + \
                    TEMP[row + 1][col + 2] + \
                    TEMP[row + 2][col + 0] + \
                    TEMP[row + 2][col + 1] + \
                    TEMP[row + 2][col + 2]

            if  row == 0 or col == 0 or row == len(M) - 1 or col == len(M[0]) - 1:
                count = 6
                if row == 0 and col == 0:
                    count = 4
                elif row == len(M) - 1 and col == len(M[0]) - 1:
                    count = 4
                elif row == 0 and col == len(M[0]) - 1:
                    count = 4
                elif row == len(M) - 1 and col == 0:
                    count = 4

            if len(M) == 1 or len(M[0]) == 1:
                count = 3
                if row == 0 or col == 0:
                    if row == 0 and col == 0:
                        count = 2
                    elif row == 0 and col == len(M[0]) - 1:
                        count = 2
                    elif row == len(M) - 1 and col == 0:
                        count = 2
                if len(M) == len(M[0]):
                    count = 1

            RES[row][col] = sum // count

        return RES

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

    data0 = flds[0].split(",")
    M = [[0 for j in range(len(data0))] for i in range(len(flds))]

    for i in range(len(flds)):
        line = flds[i].split(",")
        for j in range(len(line)):
            M[i][j] = int(line[j])
        print("M[%d] = %s" %(i, M[i]))
 
#    print("M[] = %s" %M)

    time0 = time.time()

    sl = Solution()
    result = sl.imageSmoother(M)

    time1 = time.time()

    print()
    for i in range(len(result)):
        print("M[%d] = %s" %(i, result[i]))
#    print("result = %s" %result)

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
