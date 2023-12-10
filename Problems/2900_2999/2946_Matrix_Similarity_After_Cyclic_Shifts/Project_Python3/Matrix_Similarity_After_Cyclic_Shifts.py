import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # 116ms - 124ms
        n = len(mat[0])
        for row in mat:
            for i in range(n):
                if row[i] != row[(i + k)%n]:
                    return False
        return True

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[")

    mat = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    k = int(flds[1].replace("]]", ""))
    print("mat = {0}, k = {1:d}".format(mat, k))

    sl = Solution()
    time0 = time.time()

    result = sl.areSimilar(mat, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
