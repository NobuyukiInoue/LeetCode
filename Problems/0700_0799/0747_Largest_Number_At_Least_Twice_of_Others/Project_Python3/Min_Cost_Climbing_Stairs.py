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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    cost = [int(n) for n in str_args.split(",")]
    print("cost = %s" %cost)

    time0 = time.time()

    sl = Solution()
    result = sl.minCostClimbingStairs(cost)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
