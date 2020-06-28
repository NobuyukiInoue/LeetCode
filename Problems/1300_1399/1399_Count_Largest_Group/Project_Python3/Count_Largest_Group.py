# coding: utf-8

import os
import sys
import time

import collections
import statistics

class Solution:
#   def countLargestGroup(self, n: int) -> int:
    def countLargestGroup(self, n):
        # 100ms
        # statistics.multimode was added in python3.8.
        return len(statistics.multimode(sum(map(int, str(i))) for i in range(1, n+1)))

    def countLargestGroup2(self, n):
        # 140ms
        counter = collections.Counter()
        for i in range(1, n + 1):
            counter[sum(int(j) for j in str(i))] += 1
        size = collections.Counter(counter.values())
        return size[max(size)]

    def countLargestGroup_bad(self, n):
        table = [[i] for i in range(1, n + 1)]
        lengths = [0]*n
        res = 0
        for num in range(10, n + 1):
            work_num = num
            sum_of_digits = 0
            while work_num > 0:
                sum_of_digits += work_num % 10
                work_num //= 10
            table[sum_of_digits - 1].append(num)
            lengths[sum_of_digits] += 1
        print(table)
        digits_length = max(lengths) + 1
        res = 0
        for t in table:
            if len(t) == digits_length:
                res += 1
        return res

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(flds)
    print("n = {0}".format(n))

    sl = Solution()
    time0 = time.time()
    result = sl.countLargestGroup(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
