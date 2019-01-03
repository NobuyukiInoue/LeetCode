# coding: utf-8

import os
import sys
import time

class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))
        return radius

    def findRadius_work(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius_min = [sys.maxsize]*len(houses)
        for i in range(len(houses)):
            for he in heaters:
                radius = abs(he - houses[i])
                if radius < radius_min[i]:
                    radius_min[i] = radius
        radius = 0
        for temp in radius_min:
            if temp > radius:
                radius = temp
        return radius

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    var_str = temp.replace("[[","").replace("]]","").rstrip()
    flds = var_str.split("],[")
    houses = str_to_int_array(flds[0])
    heaters = str_to_int_array(flds[1])

    time0 = time.time()

    sl = Solution()
    result = sl.findRadius(houses, heaters)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
