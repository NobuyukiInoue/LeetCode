import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # 107ms - 109ms
        n = len(A)
        cnts = [0]*(n + 1)
        C, total = [], 0
        for i in range(n):
            cnts[A[i]] += 1
            if cnts[A[i]] == 2:
                total += 1
            cnts[B[i]] += 1
            if cnts[B[i]] == 2:
                total += 1
            C.append(total)
        return C

    def findThePrefixCommonArray2(self, A: List[int], B: List[int]) -> List[int]:
        # 102ms - 113ms
        C = []
        a_mask = 0
        b_mask = 0
        for a_num, b_num in zip(A, B):
            a_mask ^= (1 << a_num)
            b_mask ^= (1 << b_num)
            C.append((a_mask & b_mask).bit_count())
        return C

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    A = [int(col) for col in flds[0].split(",")]
    B = [int(col) for col in flds[1].split(",")]
    print("A = {0}, B = {1}".format(A, B))

    sl = Solution()
    time0 = time.time()

    result = sl.findThePrefixCommonArray(A, B)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
