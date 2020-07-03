# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def average(self, salary: List[int]) -> float:
    def average(self, salary):
        # 20ms
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

    def average2(self, salary):
        # 24ms
        var_max, var_min, len_salary = max(salary), min(salary), len(salary)
        var_sum, var_count = 0, 0
        for i in range(len_salary):
            if salary[i] != var_max and salary[i] != var_min:
                var_sum += salary[i]
                var_count += 1
        return var_sum / var_count

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

    salary = [int(n) for n in flds.split(",")]
    print("salary = {0}".format(salary))

    sl = Solution()

    time0 = time.time()

    result = sl.average(salary)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
