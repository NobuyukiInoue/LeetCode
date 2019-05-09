# coding: utf-8

import os
import sys
import time

class Solution:
#    def canConstruct(self, ransomNote: 'str', magazine: 'str') -> 'bool':
    def canConstruct(self, ransomNote, magazine):
        for x in ransomNote:
            idx = magazine.find(x)
            if idx == -1:
                return False
            magazine = magazine[0:idx]+magazine[idx+1:]
                
        return True

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").rstrip().split("],[")
    ransomNote = flds[0]
    magazine = flds[1]

    print("ransomNote = %s" %ransomNote)
    print("magazine = %s" %magazine)

    time0 = time.time()

    sl = Solution()
    result = sl.canConstruct(ransomNote, magazine)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
