import os
import sys
import time

class Solution:
#   def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    def findOcurrences(self, text, first, second):
        # 24ms
        res =[]
        if not text:
            return res
        text = text.split()
        for i in range(2,len(text)):
            if text[i-2] == first and text[i-1]== second:
                res.append(text[i])
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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    text, first, second = flds[0], flds[1], flds[2]

    print("text = {0}, first = {1}, seconde = {2}".format(text, first, second))

    time0 = time.time()

    sl = Solution()
    result = sl.findOcurrences(text, first, second)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
