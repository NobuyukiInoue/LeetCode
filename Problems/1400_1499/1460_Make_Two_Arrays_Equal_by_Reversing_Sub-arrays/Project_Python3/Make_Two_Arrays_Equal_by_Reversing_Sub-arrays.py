import os
import sys
import time

class Solution:
#   def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    def canBeEqual(self, target, arr):
        # 76ms
        return sorted(target) == sorted(arr)

    def canBeEqual2(self, target, arr):
        # 84ms
        return collections.Counter(target) == collections.Counter(arr)

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    target = [int(val) for val in str_args[0].split(",")]
    arr = [int(val) for val in str_args[1].split(",")]
    print("target[] = {0}, arr = {1}".format(target, arr))

    time0 = time.time()

    sl = Solution()
    result = sl.canBeEqual(target, arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()
