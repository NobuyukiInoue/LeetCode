import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 235ms - 251ms
        total = 0
        for i, _ in enumerate(customers):
            total += customers[i]*(1 - grumpy[i])
            grumpy[i] = customers[i] * grumpy[i]
        m_custmers = 0
        for i in range(minutes):
            m_custmers += grumpy[i]
        save = m_custmers
        for i in range(minutes, len(customers)):
            save = save + grumpy[i] - grumpy[i - minutes]
            if save > m_custmers:
                m_custmers = save
        return total + m_custmers

    def maxSatisfied1(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 244ms - 249ms
        z = list(map(operator.mul, customers, grumpy))
        ans = score = sum(customers) - sum(z[minutes:])
        for i in range(len(grumpy) - minutes):
            score += z[i + minutes] - z[i]
            ans = max(ans, score)
        return ans
    
    def maxSatisfied2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 252ms - 255ms
        m_custmers, ans, tmp = 0, 0, 0
        for i , _ in enumerate(customers):
            if not grumpy[i]:
                ans += customers[i]
                customers[i] = 0
            else:
                tmp += customers[i]
            if i >= minutes:
                tmp -= customers[i - minutes]
            m_custmers = max(m_custmers, tmp)
        return ans + m_custmers

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    customers = [int(n) for n in flds[0].split(",")]
    grumpy = [int(n) for n in flds[1].split(",")]
    minutes = int(flds[2])
    print("customers = {0}, grumpy = {1}, minutes = {2:d}".format(customers, grumpy, minutes))

    sl = Solution()
    time0 = time.time()

    result = sl.maxSatisfied(customers, grumpy, minutes)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
