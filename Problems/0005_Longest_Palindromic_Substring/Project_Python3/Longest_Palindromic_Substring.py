import os
import sys
import time
from collections import deque

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
        	return ""
        maxLen = 1
        start = 0
        for i in range(len(s)):
        	if i - maxLen >= 1 and s[i - maxLen-1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
        		start = i - maxLen - 1
        		maxLen += 2
        		continue
        	if i - maxLen >= 0 and s[i - maxLen:i + 1]==s[i - maxLen:i + 1][::-1]:
        		start = i - maxLen
        		maxLen += 1

        return s[start:start + maxLen]

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = %s" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.longestPalindrome(s)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
