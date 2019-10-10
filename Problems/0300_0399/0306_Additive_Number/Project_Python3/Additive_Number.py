import math
import os
import sys
import time

class Solution:
#   def isAdditiveNumber(self, num: str) -> bool:
    def isAdditiveNumber(self, num):
        for i in range(len(num)-2):
            for j in range(i+1,len(num)):
                if self.helper(0,i,j,num):return True
        return False
    
    def helper(self, i1, i2, i3, num):
        if num[i1] == '0' and i1 != i2:
            return False
        if num[i2 + 1] == '0' and i3 != i2 + 1:
            return False
        if i3 == len(num) - 1 and not i1 == 0:
            return True
        for i in range(i3 + 1, len(num)):
            if int(num[i1:i2 + 1]) + int(num[i2 + 1:i3 + 1]) != int(num[i3 + 1:i + 1]):
                continue
            if self.helper(i2 + 1,i3, i, num):
                return True
        return False

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    num = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    print("num = %s" %num)

    time0 = time.time()

    sl = Solution()
    result = sl.isAdditiveNumber(num)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
