import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # 249ms - 283ms
        def getScore(nums: List[int]) -> int:
            score, cnt = 0, 0
            for _, num in enumerate(nums):
                if cnt > 0:
                    score += num*2
                    cnt -= 1
                else:
                    score += num
                if num == 10:
                    cnt = 2
            return score
        score1 = getScore(player1)
        score2 = getScore(player2)
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        return 0

    def isWinner_6liner(self, player1: List[int], player2: List[int]) -> int:
        # 270ms
        isTen1 = isTen2 = wasTen1 = wasTen2 = False
        diff = 0
        for n1, n2 in zip(player1, player2):
            diff += (1 + (wasTen1|isTen1))*n1 - (1 + (wasTen2|isTen2))*n2
            isTen1,isTen2, wasTen1, wasTen2 = n1 == 10, n2 == 10, isTen1, isTen2 
        return  (diff < 0) + (diff != 0)

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    player1 = [int(n) for n in flds[0].split(",")]
    player2 = [int(n) for n in flds[1].split(",")]
    print("player1 = {0}, k = {1}".format(player1, player2))

    sl = Solution()
    time0 = time.time()

    result = sl.isWinner(player1, player2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
