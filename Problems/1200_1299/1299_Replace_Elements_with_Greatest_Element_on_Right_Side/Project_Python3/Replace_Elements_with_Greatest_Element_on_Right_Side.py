import os
import sys
import time

class Solution:
#   def replaceElements(self, arr: List[int]) -> List[int]:
    def replaceElements(self, arr):
        mx = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    arr = [int(val) for val in flds.split(",")]
    print("arr = {0}".format(arr))

    time0 = time.time()

    sl = Solution()
    result = sl.replaceElements(arr)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
