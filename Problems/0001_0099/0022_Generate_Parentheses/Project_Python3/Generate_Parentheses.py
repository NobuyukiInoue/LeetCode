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
    n = int(temp)

    sl = Solution()
    time0 = time.time()

    result = sl.generateParenthesis(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
