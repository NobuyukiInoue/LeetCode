import os
import sys
import time

class Solution:
#    def reverseStr(self, s: str, k: int) -> str:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) >= 2*k:
            firstKStr = s[:k]
            return firstKStr[::-1]+s[k:2*k] + self.reverseStr(s[2*k:],k)
        elif len(s) < k:
            return s[::-1]
        else:
            firstKStr = s[:k]
            return firstKStr[::-1]+s[k:]
    
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s = flds[0]
    k = int(flds[1])
    print("s[] = %s, k = %d" %(s, k))

    time0 = time.time()

    sl = Solution()
    result = sl.reverseStr(s, k)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
