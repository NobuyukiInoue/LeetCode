import os
import sys
import time

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        size = len(flowerbed)
        if sum(flowerbed) + n > size//2 + size%2: return False
        if len(flowerbed) == 1: return True
        
        plant = 0
        for i in range(size):
            if flowerbed[i] == 1: continue
            if i != 0:
                if flowerbed[i - 1] == 1: continue
            if i != size - 1: 
                if flowerbed[i + 1] == 1: continue
            plant += 1
            flowerbed[i] = 1
        return n <= plant

    def canPlaceFlowers_work(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """ 
        if len(flowerbed) == 0:
            return False

        if n == 0:
            return True

        if len(flowerbed) >= 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
                if n == 0:
                    return True

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1: continue
            if flowerbed[i - 1] == 1: continue
            if flowerbed[i + 1] == 1: continue

            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

        if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1

        return True if n == 0 else False

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
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    flowerbed = [int(val) for val in flds[0].split(",")]
    n = int(flds[1])
    print("flowerbed = {0}, n = {1:d}".format(flowerbed, n))

    sl = Solution()
    time0 = time.time()

    result = sl.canPlaceFlowers(flowerbed, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
