import os
import sys
import time

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 28ms
        res = start
        for i in range(1, n):
            res ^= start + 2*i
        return res

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

    n, start = int(flds[0]), int(flds[1])

    print("n = {0:d}, start = {1:d}".format(n, start))

    sl = Solution()
    time0 = time.time()

    result = sl.xorOperation(n, start)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
