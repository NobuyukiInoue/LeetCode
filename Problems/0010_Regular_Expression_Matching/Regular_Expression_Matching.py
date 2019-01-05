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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    s = flds[0]
    p = flds[1]
    print("s = %s, p = %s" %(s, p))

    time0 = time.time()

    sl = Solution()
    result = sl.isMatch(s, p)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
