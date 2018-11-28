# coding: utf-8

import sys
import time

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        m = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,'CD':400, 'CM':900}
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


    def romanToInt_old(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            if i == 0:
                if s[i] == 'I':
                    sum += 1
                elif s[i] == 'V':
                    sum += 5
                elif s[i] == 'X':
                    sum += 10
                elif s[i] == 'L':
                    sum += 50
                elif s[i] == 'C':
                    sum += 100
                elif s[i] == 'D':
                    sum += 500
                elif s[i] == 'M':
                    sum += 1000
            else:
                if s[i] == 'I':
                    sum += 1
                elif s[i] == 'V' and s[i - 1] == 'I':
                    sum += 3
                elif s[i] == 'V':
                    sum += 5
                elif s[i] == 'X' and s[i - 1] == 'I':
                    sum += 8
                elif s[i] == 'X':
                    sum += 10
                elif s[i] == 'L' and s[i - 1] == 'X':
                    sum += 30
                elif s[i] == 'L':
                    sum += 50
                elif s[i] == 'C' and s[i - 1] == 'X':
                    sum += 80
                elif s[i] == 'C':
                    sum += 100
                elif s[i] == 'D' and s[i - 1] == 'C':
                    sum += 300
                elif s[i] == 'D':
                    sum += 500
                elif s[i] == 'M' and s[i - 1] == 'C':
                    sum += 800
                elif s[i] == 'M':
                    sum += 1000

        return sum        


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    s = args[1].rstrip()
    s = s.replace("\"", "")

    time0 = time.time()

    sl = Solution()
    print(sl.romanToInt(s))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
