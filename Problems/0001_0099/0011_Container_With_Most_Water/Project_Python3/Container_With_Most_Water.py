# coding: utf-8

import os
import sys
import time

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        
        ret = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > ret:
                ret = area
            # Move the lower bar until there is a higher bar
            if height[l] < height[r]:
                cur_l = l
                l += 1
                while l < r and height[l] < height[cur_l]:
                    l += 1                    
            else:
                cur_r = r
                r -= 1
                while l < r and height[r] < height[cur_r]:
                    r -= 1
            
        return ret

    def maxArea_work(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if height[i] < height[j]:
                    area = (j - i)*height[i]
                else:
                    area = (j - i)*height[j]
                if area > max_area:
                    max_area = area
                    # print("i = %d, j = %d, area = %d" %(i, j, area))
        return max_area

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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    height = [int(val) for val in flds]
    print("height = %s" %height)

    time0 = time.time()

    sl = Solution()
    result = sl.maxArea(height)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
