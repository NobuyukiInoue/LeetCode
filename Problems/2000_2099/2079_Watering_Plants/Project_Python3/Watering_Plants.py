import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # 38ms - 49ms
        ans, water = 0, capacity
        for i, p in enumerate(plants):
            if p <= water:
                water -= p
                ans += 1
            else:
                water = capacity - p
                ans += 2*i + 1
        return ans

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    plants = [int(n) for n in flds[0].split(",")]
    capacity = int(flds[1])
    print("plants = {0}, capacity = {1:d}".format(plants, capacity))

    sl = Solution()
    time0 = time.time()

    result = sl.wateringPlants(plants, capacity)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
