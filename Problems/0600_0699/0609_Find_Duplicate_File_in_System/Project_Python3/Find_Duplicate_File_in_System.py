import collections
import os
import sys
import time

class Solution:
#   def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    def findDuplicate(self, paths):
        # 92ms
        M = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                M[content[:-1]].append(root + '/' + name)
        return [x for x in M.values() if len(x) > 1]

    def findDuplicate2(self, paths):
        # Time Limit Exceeded
        index, names, contents = 0, {}, {}
        for path in paths:
            flds = path.split(" ")
            for j in range(1, len(flds)):
                if not "/" in flds[j]:
                    flds[j] = flds[0] + "/" + flds[j]
                data = flds[j].split("(")
                data[1] = data[1][:-1]
                names[index] = data[0]
                contents[index] = data[1]
                index += 1
        res = [[] for i in range(len(contents))]
        index = 0
        for i in range(len(contents) - 1):
            if contents[i] == "":
                continue
            hit = False
            for j in range(i + 1, len(contents)):
                if contents[j] == "":
                    continue
                if contents[j] == contents[i]:
                    hit = True
                    if len(res[index]) == 0:
                        res[index].append(names[i])
                    res[index].append(names[j])
                    contents[j] = ""
            if hit:
                index += 1

        return res[:index]

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
    paths = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    print("paths = {0}".format(paths))

    sl = Solution()
    time0 = time.time()
    result = sl.findDuplicate(paths)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
