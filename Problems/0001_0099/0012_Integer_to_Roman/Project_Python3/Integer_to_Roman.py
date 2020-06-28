# coding: utf-8

import os
import sys
import time

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman = ''
        for i, s in roman_dict.items():
            roman += num // i * s
            num %= i
        return roman

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        m = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC': 90, 'L':50, 'XL': 40, 'X':10, 'IX': 9, 'V':5, 'IV': 4, 'I':1}
    #   print(m)
        i = 0
        while i < len(s):
            if i < len(s)-1: 
                if s[i:i+2] in m:
                    num += m[s[i:i+2]]
                    i += 2
                    continue
        #   print(i)
            num += m[s[i]]
            i += 1
        return num

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
    num = int(temp.replace("[","").replace("]","").rstrip())
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.intToRoman(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
