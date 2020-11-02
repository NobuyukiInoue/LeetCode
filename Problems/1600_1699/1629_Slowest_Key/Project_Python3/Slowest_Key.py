import os
import sys
import time

class Solution:
#   def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    def slowestKey(self, releaseTimes, keysPressed):
        # 48ms
        maxDiff = releaseTimes[0]
        result = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            if diff >= maxDiff:
                currChar = keysPressed[i]
                if diff > maxDiff or currChar > result:
                    result = currChar
                maxDiff = diff
        return result

    def slowestKey2(self, releaseTimes, keysPressed):
        # 52ms
        for i, (k, t) in enumerate(zip(keysPressed, releaseTimes)):
            res = max(res, ((t - releaseTimes[i-1]), k)) if i != 0 else (t, k)
        return res[1]

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[")
    releaseTimesStr = flds[0].replace("[[", "")
    releaseTimes = [int(n) for n in releaseTimesStr.split(",")]
    keysPressed = flds[1].replace("]]", "")

    print("releaseTimes[] = {0}".format(releaseTimes))
    print("keysPressed  = {0}".format(keysPressed))

    sl = Solution()
    time0 = time.time()

    result = sl.slowestKey(releaseTimes, keysPressed)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
