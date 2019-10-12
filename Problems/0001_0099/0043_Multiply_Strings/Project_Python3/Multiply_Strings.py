# coding: utf-8

import os
import sys
import time

class Solution:
#   def multiply(self, num1: str, num2: str) -> str:
    def multiply(self, num1, num2):
        # 40ms
        v_num1 = [0]*len(num1)
        for i in range(len(num1)):
            v_num1[i] = ord(num1[i]) - ord('0')
        v_num2 = [0]*len(num2)
        for i in range(len(num2)):
            v_num2[i] = ord(num2[i]) - ord('0')

        val1 = 0
        for n in v_num1:
            val1 *= 10
            val1 += n

        result = 0
        for m in v_num2:
            result *= 10
            result += val1 * m 

        return str(result)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    num1 = flds[0]
    num2 = flds[1]
    print("num1 = {0}, num2 = {1}".format(num1, num2))

    time0 = time.time()

    sl = Solution()
    result = sl.multiply(num1, num2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
