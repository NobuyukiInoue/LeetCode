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

    if (argc < 2):
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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    N = int(flds)

    print("N = %d\n" %N)

    time0 = time.time()

    sl = Solution()
    result = sl.rotatedDigits(N)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
