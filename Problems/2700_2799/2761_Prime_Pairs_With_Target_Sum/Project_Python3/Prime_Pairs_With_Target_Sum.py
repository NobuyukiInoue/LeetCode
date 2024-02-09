import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # 2569ms - 2580ms
        lst = [False] * (n + 1)
        for i in range(2, int(n**0.5) + 1):
            if not lst[i]:
                for j in range(2 * i, n + 1, i):
                    lst[j] = True
        ans = []
        for i in range(2, n // 2 + 1):
            x, y = i, n - i
            if not lst[x] and not lst[y] and x <= y:
                ans.append([x, y])
        return ans

    def findPrimePairs_bad(self, n: int) -> List[List[int]]:
        # Time Limite Exceeded. 499 / 554
        def is_prime(n: int) -> bool:
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        def get_primes(n: int) -> List[int]:
            return [2] + [3] + [i for i in range(3, n, 2) if is_prime(i)]

        primes = get_primes(n)
        return [[prime, n - prime] for i, prime in enumerate(primes) if n - prime in primes[i:]]

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
    fld = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(fld)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.findPrimePairs(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
