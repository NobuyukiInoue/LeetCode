import os
import sys
import time

class Solution:
#   def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    def kidsWithCandies(self, candies, extraCandies):
        # 32ms
        return [num + extraCandies >= max(candies) for num in candies]

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    candies = [int(val) for val in str_args[0].split(",")]
    extraCandies = int(str_args[1])
    print("candies[] = {0}, extraCandies = {1}".format(candies, extraCandies))

    sl = Solution()
    time0 = time.time()
    result = sl.kidsWithCandies(candies, extraCandies)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
