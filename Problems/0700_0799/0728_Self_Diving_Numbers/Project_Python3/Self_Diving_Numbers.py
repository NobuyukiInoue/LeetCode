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

    if (argc < 2):
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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    left, right = int(flds[0]), int(flds[1])

    print("left = %d, right = %d\n" %(left, right))

    time0 = time.time()

    sl = Solution()
    result = sl.selfDividingNumbers(left, right)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
