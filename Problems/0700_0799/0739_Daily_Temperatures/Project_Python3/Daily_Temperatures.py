import os
import sys
import time

class Solution:
#   def dailyTemperatures(self, T: List[int]) -> List[int]:
    def dailyTemperatures(self, T):
        # 472ms
        len_T = len(T)
        counts = [0] * len_T
        for k in range(len_T-2,-1,-1):
            j = k+1
            while True:
                if T[k] >= T[j] and counts[j] == 0:
                    break
                elif T[k] < T[j]:
                    counts[k] = j-k
                    break
                else:
                    j = j + counts[j] 
        return counts

    def dailyTemperatures2(self, T):
        # 504ms
        stack = []
        res = [0] * len(T)
        
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                prevIndex = stack[-1][1]
                diff = i - prevIndex
                res[prevIndex] = diff
                stack.pop()
            stack.append((t, i))
        return res

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    T = [int(val) for val in flds.split(",")]
    print("T = {0}".format(T))

    sl = Solution()
    time0 = time.time()
    result = sl.dailyTemperatures(T)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
