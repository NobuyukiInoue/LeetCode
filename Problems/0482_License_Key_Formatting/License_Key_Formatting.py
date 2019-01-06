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

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    S = str_args[0]
    K = int(str_args[1])
    print("S = %s, K = %d" %(S, K))

    time0 = time.time()

    sl = Solution()
    result = sl.licenseKeyFormatting(S, K)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
