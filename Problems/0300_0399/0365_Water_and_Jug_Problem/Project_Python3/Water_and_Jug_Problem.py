import math
import os
import sys
import time

class Solution:
#   def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    def canMeasureWater(self, x, y, z):
        # 16ms
        if z > x + y:
            return False
        try:
            return z % math.gcd(x, y) == 0
        except ZeroDivisionError:
            return z == 0

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    x, y, z = int(flds[0]), int(flds[1]), int(flds[2])
    print("x = {0:d}, y = {1:d}, z = {2:d}".format(x, y, z))

    time0 = time.time()

    sl = Solution()
    result = sl.canMeasureWater(x, y, z)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
