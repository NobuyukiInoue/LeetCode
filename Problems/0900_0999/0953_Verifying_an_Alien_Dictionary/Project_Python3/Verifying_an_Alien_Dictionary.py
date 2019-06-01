import math
import os
import sys
import time

class Solution:
#   def isAlienSorted(self, words: List[str], order: str) -> bool:
    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

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
    flds = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    words = flds[0].split(",")
    order = flds[1]
    print("words = %s, order = %s" %(words, order))

    time0 = time.time()

    sl = Solution()
    result = sl.isAlienSorted(words, order)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
