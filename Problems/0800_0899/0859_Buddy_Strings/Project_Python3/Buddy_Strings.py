import math
import os
import sys
import time

class Solution:
#   def buddyStrings(self, A: str, B: str) -> bool:
    def buddyStrings(self, A, B):
        if len(A) != len(B) or len(A) < 2 or len(B) < 2:
            return False

        if A == B:
            return len(A) != len(set(A))
        
        A = list(A)
        B = list(B)
        
        indexes = []
        
        for index in range(len(A)):
            if len(indexes) > 2:
                return False
            
            if A[index] != B[index]:
                indexes.append(index)

        if len(indexes) != 2:
            return False
                
        temp = A[indexes[0]]
        A[indexes[0]] = A[indexes[1]]
        A[indexes[1]] = temp
        
        return A == B

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
    words = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    A = words[0]
    B = words[1]
    print("A = {0}, B = {1}".format(A, B))

    sl = Solution()
    time0 = time.time()
    result = sl.buddyStrings(A, B)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
