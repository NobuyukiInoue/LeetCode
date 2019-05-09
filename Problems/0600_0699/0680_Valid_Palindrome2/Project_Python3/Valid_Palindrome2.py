# coding: utf-8

import os
import sys
import time

class Solution:
#    def validPalindrome(self, s: str) -> bool:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        if not s == s[::-1]:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    str1 = s[:left] + s[left+1:]
                    str2 = s[:right] + s[right+1:]
                    return str1 == str1[::-1] or str2 == str2[::-1]
        else:
            return True

#    def validPalindrome(self, s: str) -> bool:
    def validPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        b = s[::-1]

        for i in range(0,len(s)):
            if s[i] != b[i]:
                temp = s[:i] + s[i+1:]
                temp1 = b[:i] + b[i+1:]

        return temp == temp[::-1] or temp1 == temp1[::-1]

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    s = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    print("s = %s" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.validPalindrome(s)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
