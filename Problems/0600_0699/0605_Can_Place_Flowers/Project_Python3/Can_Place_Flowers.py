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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    flowerbed = str_to_int_array(str_args[0])
    n = int(str_args[1])
    print("flowerbed[] = %s, n = %d" %(flowerbed, n))

    time0 = time.time()

    sl = Solution()
    result = sl.canPlaceFlowers(flowerbed, n)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
