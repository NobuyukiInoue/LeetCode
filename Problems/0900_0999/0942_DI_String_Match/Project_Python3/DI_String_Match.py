import math
import os
import sys
import time

class Solution:
#   def diStringMatch(self, S: str) -> List[int]:
    def diStringMatch(self, S):
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    S = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    print("S = %s" %S)

    time0 = time.time()

    sl = Solution()
    result = sl.diStringMatch(S)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
