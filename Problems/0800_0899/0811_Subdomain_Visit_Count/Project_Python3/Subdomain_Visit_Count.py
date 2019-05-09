# coding: utf-8

import collections
import os
import sys
import time

class Solution:
    def subdomainVisits2(self, cpdomains):
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split()
            c[d] += int(n)
            for i in range(len(d)):
                if d[i] == '.': c[d[i + 1:]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]

#    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    def subdomainVisits(self, cpdomains):
        if len(cpdomains) <= 0:
            return ""

        dic = {}
        for target in cpdomains:
            count, domain = target.split(" ")

            pos = 0
            while True:
                if not domain in dic:
                    dic[domain] = int(count)
                else:
                    dic[domain] += int(count)

                pos = domain.find(".")
                if pos >= 0:
                    domain = domain[pos + 1:]
                else:
                    break

        result = []
        for key, value in dic.items():
            result.append(str(value) + " " + key)

        return result

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(", ",",").rstrip()
    cpdomains = flds.split(",")

    print("cpdomains = %s" %cpdomains)

    time0 = time.time()

    sl = Solution()
    result = sl.subdomainVisits(cpdomains)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
