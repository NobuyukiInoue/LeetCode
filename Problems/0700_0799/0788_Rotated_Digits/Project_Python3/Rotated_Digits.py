import math
import os
import sys
import time

class Solution:
#    def rotatedDigits(self, N: int) -> int:
    def rotatedDigits(self, N):
        counts = 0
        for num in range(1, N+1):
            number = str(num)
            if '3' in number or '7' in number or '4' in number: # This will be an invalid number upon rotation
                continue # Skip this number and go to next iteration
            if '2' in number or '5' in number or '6' in number or '9' in number:
                counts += 1
        return counts
        
    def rotatedDigits2(self, N):
        changed = {'2', '5', '6', '9'}
        valid = changed | {'0', '1', '8'}
        return sum(bool(set(str(i)) <= valid and set(str(i)) & changed)
                for i in range(1, N+1))


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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    N = int(flds)
    print("N = {0:d}\n".format(N))

    sl = Solution()
    time0 = time.time()

    result = sl.rotatedDigits(N)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
