import os
import sys
import time
from collections import deque

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2**31 - 1
        int_min = -2**31
        
        digits = '0123456789'
        sign = 1
        num_str = ''
        
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        if str[0] == '+':
            sign = 1
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]
            
        for s in str:
            if s in digits:
                num_str += s
            else:
                break   
        if len(num_str) == 0:
            return 0
        num = int(num_str) * sign
        
        if num > int_max: return int_max
        if num < int_min: return int_min
        
        return num

    def myAtoi_work(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        neg = False
        x = 0
        for i in range(len(str)):
            if i == 0 and str[0] == '-':
                neg = True
                continue
            if i == 0 and str[0] == '+':
                continue
            if str[i] < '0' or str[i] > '9':
                break
            x = x * 10 + int(str[i]) - int('0')
            if x > 2**31 - 1:
                if neg:
                    if x > 2**31:
                        return -(2**31)
                else:
                    return 2**31 - 1
        if neg:
            return -x
        else:
            return x

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
    print("str = {0}".format(flds))

    sl = Solution()
    time0 = time.time()

    result = sl.myAtoi(flds)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
