import collections
import os
import sys
import time

class Solution:
#   def countBits(self, num: int) -> List[int]:
    def countBits(self, num):
        # 76ms
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i>>1]+(i&1))
        return res

#   def countBits_work(self, num: int) -> List[int]:
    def countBits_work(self, num):
        # 224ms
        res = []
        for n in range(num + 1):
            res.append(self.bits(n))
        return res

    def bits(self, num):
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num //= 2
        return count

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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()
    result = sl.countBits(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
