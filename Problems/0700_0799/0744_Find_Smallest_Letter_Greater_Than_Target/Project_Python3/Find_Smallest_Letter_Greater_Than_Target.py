# coding: utf-8

import os
import sys
import time

class Solution:
    #def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetter(self, letters, target) -> str:
        if not letters:
            return "a"
        l = 0
        r = len(letters)-1
        while (l<r-1):
            mid = (l+r)//2
            if (letters[mid]<= target):
                l = mid+1
            else:
                r = mid
        if letters[l] > target:
            return letters[l]
        elif letters[r] > target:
            return letters[r]
        else:
            return letters[0]

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
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    letters = flds[0].split(",")
    target = flds[1]
    print("letters = %s" %letters)
    print("target = %s" %target)

    time0 = time.time()

    sl = Solution()
    result = sl.nextGreatestLetter(letters, target)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
