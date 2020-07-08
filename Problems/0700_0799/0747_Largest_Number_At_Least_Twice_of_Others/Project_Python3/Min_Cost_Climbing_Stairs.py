import os
import sys
import time

class Solution:
#    def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        # 48ms
        a,b = cost[0], cost[1]
        for i in range(2, len(cost)+1):
            if i !=len(cost):
                c = min(a, b) + cost[i]
                a = b
                b = c
            else:
                c = min(a, b) + 0
        return c

#    def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        # 48ms
        for i in range(2, len(cost)): 
            cost[i] += min(cost[i - 1],cost[i - 2])
        return min(cost[-1], cost[-2])

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    cost = [int(n) for n in flds.split(",")]
    print("cost = {0}".format(cost))

    sl = Solution()
    time0 = time.time()

    result = sl.minCostClimbingStairs(cost)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
