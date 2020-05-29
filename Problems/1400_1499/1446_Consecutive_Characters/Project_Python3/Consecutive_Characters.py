import itertools
import os
import sys
import time

class Solution:
#   def maxPower(self, s: str) -> int:
    def maxPower(self, s):
        # 44ms
        s_ch = s[0]
        max_count, count = 1, 1
        for ch in s[1:]:
            if ch == s_ch:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                s_ch = ch
                count = 1
        return max_count

    def maxPower2(self, s):
        # 52ms
        return max(len(list(b)) for a, b in itertools.groupby(s))

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    time0 = time.time()

    sl = Solution()
    result = sl.maxPower(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
