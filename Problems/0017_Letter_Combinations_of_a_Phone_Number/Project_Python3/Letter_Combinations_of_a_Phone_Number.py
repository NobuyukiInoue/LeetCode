import os
import sys
import time
from collections import deque

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        my_dic = {1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if not digits:
            return []
        res = []
        for digit in digits:
            if not res:
                res = [x for x in my_dic[int(digit)]]
            else:
                res = [y + x for y in res for x in my_dic[int(digit)]]
        return res

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
    digits = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("digits = %s" %digits)

    time0 = time.time()

    sl = Solution()
    result = sl.letterCombinations(digits)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
