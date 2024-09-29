import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        # 32ms - 50ms
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]

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
    
    height, threshold = [int(num) for num in flds[0].split(",")], int(flds[1])
    print("height = {0}, threshold = {1:d}".format(height, threshold))

    sl = Solution()
    time0 = time.time()

    result = sl.stableMountains(height, threshold)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()