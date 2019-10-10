import math
import os
import sys
import time

class Solution:
#    def toGoatLatin(self, S: str) -> str:
    def toGoatLatin(self, S):
        # 36ms
        vowel = set('aeiouAEIOU')
        def latin(w, i):
            if w[0] not in vowel:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i + 1)
        return ' '.join(latin(w, i) for i, w in enumerate(S.split()))

    def toGoatLatin2(self, S):
        # 48ms
        return ' '.join((w if w[0].lower() in 'aeiou' else w[1:] + w[0]) + 'ma' + 'a' * (i + 1) for i, w in enumerate(S.split()))

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    S = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    print("S = %s" %S)

    time0 = time.time()

    sl = Solution()
    result = sl.toGoatLatin(S)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
