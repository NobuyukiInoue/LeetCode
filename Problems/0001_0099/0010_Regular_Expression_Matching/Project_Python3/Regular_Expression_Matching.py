import os
import sys
import time
from collections import deque

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 40ms
        return self.isMatch2(s, p, {("",""):True})

    def isMatch2(self, s, p, memo):
        if not p and s:
            return False
        if not s and p:
            return set(p[1::2]) == {"*"} and not (len(p) % 2)
        if (s, p) in memo:
            return memo[s,p]

        char, exp, prev = s[-1], p[-1], 0 if len(p) < 2 else p[-2]
        memo[s,p] =\
               (exp == '*' and ( \
                   (prev in {char, '.'} and self.isMatch2(s[:-1], p, memo)) \
                   or self.isMatch2(s, p[:-2], memo))) \
                   or (exp in {char, '.'} and self.isMatch2(s[:-1], p[:-1], memo) \
               )

        return memo[s,p]

    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Time Exceeded
        return self.isMatch2(s, p, 0, 0)
    
    def isMatch2(self, s, p, i, j):
        if j >= len(p):
            return i >= len(s) and j >= len(p)
        if j + 1 < len(p) and p[j + 1] == '*':
            while i < len(s) and s[i] == p[j] or p[j] == '.':
                if self.isMatch2(s, p, i, j + 2):
                    return True
                i += 1
            return self.isMatch2(s, p, i, j + 2)
        elif i < len(s) and s[i] == p[j] or p[j] == '.':
            return self.isMatch2(s, p, i + 1, j + 1)
        return False
    '''

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    s, p = flds[0], flds[1]
    print("s = {0}, p = {1}".format(s, p))

    sl = Solution()
    time0 = time.time()

    result = sl.isMatch(s, p)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
