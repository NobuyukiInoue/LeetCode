# coding: utf-8

import os
import sys
import time

class Solution:
#   def restoreIpAddresses(self, s: str) -> List[str]:
    def restoreIpAddresses(self, s):
        # 44ms
        len_s = len(s)
        self.res = []
        def f(index, ip_address, bits):
            if index > len_s or bits > 32:
                return
            if index == len_s and bits == 32:
                self.res.append(ip_address[: -1])
            for i in range(index, min(len_s, index + 3)):
                if int(s[index: i + 1]) <= 255:
                    if len(s[index: i + 1]) > 1 and s[index: i + 1][0] == "0":
                        continue
                    f(i + 1, ip_address + s[index: i + 1] + ".", bits + 8)
                        
        f(0, "", 0)
        return self.res

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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    time0 = time.time()

    sl = Solution()
    result = sl.restoreIpAddresses(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
