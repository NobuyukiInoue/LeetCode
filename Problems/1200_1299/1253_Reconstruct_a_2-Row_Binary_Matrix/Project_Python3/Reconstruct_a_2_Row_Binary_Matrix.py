# coding: utf-8

from collections import defaultdict
import os
import sys
import time

class Solution:
#   def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    def reconstructMatrix(self, upper, lower, colsum):
        # 760ms
        n = len(colsum)
        if upper < 0 or lower < 0 or upper + lower != sum(colsum):
            return []
			
        row1, row2 = [0] * n, [0] * n  
        for i in range(n):
            if colsum[i] == 2:
                row1[i] = 1
                row2[i] = 1
                upper -= 1
                lower -= 1
            if upper < 0 or lower < 0:
                return []      
        i = 0
        while upper > 0 or lower > 0:
            if colsum[i] == 1:
                if upper > 0:
                    row1[i] = 1
                    upper -= 1
                else:
                    row2[i] = 1
                    lower -= 1
            i += 1
        return [row1, row2]

    def reconstructMatrix_work(self, upper, lower, colsum):
        # 784ms, 792ms
        data = [[0 for j in range(len(colsum))] for i in range(2)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                data[0][i], data[1][i] = 1, 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    data[0][i] = 1
                    upper -= 1
                else:
                    data[1][i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return None
        return data

    def reconstructMatrix2(self, upper, lower, colsum):
        # 880ms
        matrix = [[ 0 for i in range(len(colsum))] for j in range(2)]
        matsum = sum(colsum)
        if matsum != upper+lower:
            return []
        colsum_counter = {}
        for i in range(3):
            colsum_counter[i] = 0
        for i in colsum:
            colsum_counter[i] +=1
        upper_counter = upper - colsum_counter[2]
        lower_counter = lower - colsum_counter[2]
        for col in range(len(colsum)):
            if colsum[col] == 2:
                matrix[0][col]=1
                matrix[1][col]=1
            elif colsum[col] ==0:
                continue
            else:
                if upper_counter>0:
                    matrix[0][col]=1
                    matrix[1][col]=0
                    upper_counter-=1
                else:
                    matrix[0][col]=0
                    matrix[1][col]=1
                    lower_counter -=1
        if lower_counter != 0:
            return []
        return matrix

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace(" ","").replace("\"","").replace("]]","").rstrip()
    flds = str_args.split(",[")

    fld0 = flds[0].replace("[","").split(",")
    upper, lower = int(fld0[0]), int(fld0[1])
    print("uper = {0:d}, lower = {1:d}".format(upper, lower))

    colsum = [int(data) for data in flds[1].split(",")]
    print("colsum = {0}".format(colsum))

    sl = Solution()
    time0 = time.time()
    result = sl.reconstructMatrix(upper, lower, colsum)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
