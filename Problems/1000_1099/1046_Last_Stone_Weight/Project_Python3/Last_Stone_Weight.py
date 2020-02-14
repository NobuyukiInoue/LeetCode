# coding: utf-8

import os
import sys
import time

class Solution:
#   def lastStoneWeight(self, stones: List[int]) -> int:
    def lastStoneWeight(self, stones):
        while(len(stones) > 1):
            stones = sorted(stones)
            n = len(stones)
            if stones[n-1] ==  stones[n-2]:
                p = stones[n-1]
                q = stones[n-2]
                stones.remove(p)
                stones.remove(q)

            elif stones[n-2] < stones[n-1]:
                p = stones[n-2]
                stones[n-1] -= p
                stones.remove(p)
        if len(stones) > 0:
            return (stones[0])
        else:
            return 0

    def lastStoneWeight1(self, stones):
        # 40ms
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones = stones[2:]
            else:
                stones = [stones[0] - stones[1]]  + stones[2:]
                stones.sort(reverse=True)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

    def lastStoneWeight2(self, stones):
        # 32ms
        while(len(stones)>1):
            stones = sorted(stones) #We sort them in INCREASING ORDER
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2]=stones[-1]-stones[-2]
                stones.pop()
        try: return stones[0]
        except: return 0

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    stones = [int(num) for num in flds]
    print("stones = {0}".format(stones))

    time0 = time.time()

    sl = Solution()
    result = sl.lastStoneWeight(stones)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
