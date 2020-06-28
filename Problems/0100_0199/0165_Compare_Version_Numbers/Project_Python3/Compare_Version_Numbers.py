import os
import sys
import time

class Solution:
#   def compareVersion(self, version1: str, version2: str) -> int:
    def compareVersion(self, version1, version2):
        # 24ms
        str1, str2 = [int(n) for n in version1.split(".")], [int(m) for m in version2.split(".")]
        for i in range(max(len(str1), len(str2))):
            if i < len(str1):
                v1 = str1[i]
            else:
                v1 = 0
            if i < len(str2):
                v2 = str2[i]
            else:
                v2 = 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
 
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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    version1, version2 = flds[0], flds[1]

    print("version1 = {0}, version2 = {1}".format(version1, version2))

    sl = Solution()
    time0 = time.time()
    result = sl.compareVersion(version1, version2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
