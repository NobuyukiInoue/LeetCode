# coding: utf-8

import os
import sys
import time

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_length = len(g) - 1
        gave_cookies = 0
        for select_cookie in s:
            if gave_cookies > g_length:
                break
            elif g[gave_cookies] <= select_cookie:
                gave_cookies += 1
        return gave_cookies

    def findContentChildren2(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child  = 0
        cookie = 0
        while  child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]: 
                child += 1
            cookie += 1
        return child

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
    var_str = temp.replace("[[","").replace("]]","").rstrip()
    flds = var_str.split("],[")

    g = [int(val) for val in flds[0].split(",")]
    s = [int(val) for val in flds[1].split(",")]
    print("g = %s" %g)
    print("s = %s" %s)

    time0 = time.time()

    sl = Solution()
    result = sl.findContentChildren(g, s)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
