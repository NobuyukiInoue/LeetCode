# coding: utf-8

import os
import sys
import time

class Solution:
#   def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n):
        # 52ms
        return [(not i%3)*"Fizz" + (not i%5)*"Buzz" or str(i) for i in range(1, n+1)]

    def fizzBuzz2(self, n):
        # 52ms
        results = [""]*n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                results[i - 1] = "Fizz"
            elif i % 5 == 0:
                results[i - 1] = "Buzz"
            else:
                results[i - 1] = str(i)
        return results

    def fizzBuzz3(self, n):
        # 52ms
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append("FizzBuzz")
            elif i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))
        return results

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0}".format(n))

    time0 = time.time()

    sl = Solution()
    result = sl.fizzBuzz(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
