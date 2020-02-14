# coding: utf-8

from collections import defaultdict
import os
import sys
import time

class Solution:
#   def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    def smallestStringWithSwaps(self, s: str, pairs):
        # 720ms
        def get_parent(i):
            while union[i] != i:
                i = union[i]
            return i
        union = [i for i in range(len(s))]
        for i, j in pairs:
            i = get_parent(i)
            j = get_parent(j)
            if i > j:
                i, j = j, i
            union[i] = j
        parent_childs = {}
        for i in range(len(s)):
            j = get_parent(union[i])
            parent_childs[j] = parent_childs.get(j, set())
            parent_childs[j].add(i)
        res = [0 for _ in range(len(s))]
        for i in parent_childs:
            for j, k in zip(sorted(parent_childs[i]), sorted([s[m] for m in parent_childs[i]])):
                res[j] = k
        return "".join(res)

    def smallestStringWithSwaps2(self, s: str, pairs):
        # 912ms
        class UF:
            def __init__(self, n):
                self.p = list(range(n))
            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf, res, m = UF(len(s)), [], defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)

    def smallestStringWithSwaps_work(self, s: str, pairs):
        """
        pairs.sort()
        print("pais = {0}".format(pairs))
        """
        hit = True
        while hit:
            hit = False
            for pos in pairs:
                if ord(s[pos[0]]) > ord(s[pos[1]]):
                    s = s[:pos[0]] + s[pos[1]] + s[pos[0]+1:pos[1]] + s[pos[0]] + s[pos[1]+1:]
                    hit = True
        return s

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("]]]","").rstrip()
    flds = str_args.split("],[[")

    s = flds[0].replace("[","")
    print("s = {0}".format(s))

    pairs = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    print("pairs = {0}".format(pairs))

    time0 = time.time()

    sl = Solution()
    result = sl.smallestStringWithSwaps(s, pairs)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
