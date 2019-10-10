# coding: utf-8

import os
import sys
import time

class Solution:
  #  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def floodFill(self, image, sr, sc, newColor):
        def helper(i, j, comp):
            if 0 <= i < len(image) and 0 <= j < len(image[i]):
                if image[i][j] == comp:
                    image[i][j] = newColor
                    helper(i - 1, j, comp)
                    helper(i, j - 1, comp)
                    helper(i + 1, j, comp)
                    helper(i, j + 1, comp)
        if sr < len(image) and sc < len(image[sr]) and image[sr][sc] != newColor:
            helper(sr, sc, image[sr][sc])
        return image

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
    flds = temp.replace("[[[","").replace("\"","").replace(" ","").rstrip().split("]],[")
    arr1 = flds[0].split("],[")
    arr2 = flds[1].replace("]]", "").split("],[")

    image = [[0 for i in range(3)] for j in range(len(arr1))]
    for i in range(len(arr1)):
        temp = arr1[i].split(",")
        for j in range(len(temp)):
            image[i][j] = int(temp[j])

    sr = int(arr2[0])
    sc = int(arr2[1])
    newColor = int(arr2[2])

    print("image = %s" %image)
    print("sr = %d, sc = %d, newColor = %d" %(sr, sc, newColor))

    time0 = time.time()

    sl = Solution()
    result = sl.floodFill(image, sr, sc, newColor)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
