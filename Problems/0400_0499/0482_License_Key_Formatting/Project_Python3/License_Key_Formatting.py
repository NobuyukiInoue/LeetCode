import os
import sys
import time

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        clean = S.replace("-", "").upper()
        groups = []
        if len(clean) % K != 0:
            groups.append(clean[:len(clean) % K])
        for i in range(len(clean) % K, len(clean) - K + 1, K):
            groups.append(clean[i:i+K])
        return  "-".join(groups)

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    S = flds[0]
    K = int(flds[1])
    print("S = {0}, K = {1:d}".format(S, K))

    sl = Solution()
    time0 = time.time()

    result = sl.licenseKeyFormatting(S, K)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
