# coding: utf-8

import os
import sys
import time

class Solution:
    def convertToTitle(self, n):
        if n < 1:
            return ""

        temp = n - 1
        # print("temp = %s" %temp)

        target = []
        while True:
            mod = temp % 26
            # print("mod = %s" %mod)
            target.append(mod)
            temp -= mod
            if temp >= 26:
                temp = int(temp / 26) - 1
                continue
            else:
                break
            
        result = ""

        for i in range(len(target)):
            result = chr(ord('A') + target[i]) + result
            # print("target[%s] = %s" %(i, target[i]))
            # print("result = %s" %result)

        return result

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
    str_args = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(str_args)
    print("n = %s" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.convertToTitle(n)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
