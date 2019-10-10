# coding: utf-8

import os
import sys
import time

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def backtrack(S = '', left = 0, right = 0):
            if(len(S) == 2*n):
                ans.append(S)
                return
            
            if(left < n):
                backtrack(S + "(", left + 1, right)
                
            if(left > right and right < n):
                backtrack(S + ")", left, right + 1)
            
        backtrack()
        return ans

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

def loop_main(temp):
    n = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.generateParenthesis(n)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
