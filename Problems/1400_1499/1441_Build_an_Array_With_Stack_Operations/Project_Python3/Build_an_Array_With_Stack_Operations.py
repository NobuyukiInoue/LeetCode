import os
import sys
import time

class Solution:
#   def buildArray(self, target: List[int], n: int) -> List[str]:
    def buildArray(self, target, n):
        # 24ms-36ms
        res = []
        pos, i = 1, 0
        while i < len(target):
            if target[i] == pos:
                res.append("Push")
                i += 1
            else:
                res.append("Push")
                res.append("Pop")
            pos += 1
        return res

    def buildArray2(self, target, n):
        # 28ms-32ms
        res, pos = [], 0
        for i in range(1, n + 1):
            if pos >= len(target):
                break 
            if target[pos] == i:
                res.append("Push")
                pos += 1
            else:
                res.append("Push")
                res.append("Pop")
        return res

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
    n = int(str_args[1])
    print("target[] = {0}, n = {1}".format(target, n))

    time0 = time.time()

    sl = Solution()
    result = sl.buildArray(target, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()
