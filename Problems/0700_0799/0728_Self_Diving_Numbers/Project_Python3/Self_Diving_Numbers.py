import os
import sys
import time

class Solution:
#    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def selfDividingNumbers(self, left, right):
        res = []
        n = 0
        for i in range(left, right + 1):
            n = i
            while n > 0:
                if n % 10 == 0 or i % (n % 10) != 0:
                    break
                n //= 10
            if n == 0:
                res.append(i)
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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    left, right = int(flds[0]), int(flds[1])
    print("left = {0:d}, right = {1:d}\n".format(left, right))

    sl = Solution()
    time0 = time.time()

    result = sl.selfDividingNumbers(left, right)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
