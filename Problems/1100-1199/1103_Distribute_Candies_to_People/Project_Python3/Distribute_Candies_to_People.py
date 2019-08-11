# coding: utf-8

import os
import sys
import time

class Solution:
#   def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    def distributeCandies(self, candies, num_people):
        results = [0]*num_people
        sum = 0
        for i in range(1, candies + 1):
            if sum + i > candies:
                results[(i - 1)%num_people] += candies - sum
                return results
            else:
                results[(i - 1)%num_people] += i
                sum += i
 
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    candies = int(flds[0])
    num_people = int(flds[1])

    time0 = time.time()

    sl = Solution()
    result = sl.distributeCandies(candies, num_people)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
