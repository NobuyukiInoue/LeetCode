# coding: utf-8

import os
import sys
import time
import collections

class Solution:
#   def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def findOrder(self, numCourses, prerequisites):
        # 104ms
        graph = collections.defaultdict(list)
        in_degree = {k: 0 for k in range(numCourses)}
        for to, frm in prerequisites:
            graph[frm].append(to)
            in_degree[to] += 1
        queue = collections.deque([node for node in in_degree if in_degree[node] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for node in graph[node]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)
        return order if len(order) == numCourses else []

    def findOrder2(self, numCourses, prerequisites):
        # 108ms
        def helper(vertex):
            # False means visiting, True means visited
            visited[vertex] = False
            for v in graph[vertex]:
                # we have detected a cycle in the graph, directly return False
                if v in visited and visited[v] is False:
                    return False
                # we have seen this vertex before and it is been fully discovered, return True, in this problem this means two courses depends on the same course
                if v in visited and visited[v] is True:
                    continue
                if not helper(v):
                    return False
            order.append(vertex)
            visited[vertex] = True
            return True
            
        graph = {i: [] for i in range(numCourses)}
        for p in prerequisites:
            graph[p[0]].append(p[1])
        order = []
        visited = {}
        for vert in graph.keys():
            if vert in visited:
                continue
            if not helper(vert):
                return []
        return order

    def findOrder_bad(self, numCourses, prerequisites):
        # xxms
        if len(prerequisites) == 0:
            return [n for n in range(numCourses)]
        if len(prerequisites[0]) == 0:
            return [n for n in range(numCourses)]

        G = [[] for i in range(numCourses)]
        for j, i in prerequisites:
            G[i].append(j)
        res = []
        for i in range(len(G)):
            if len(G[i]) > 0 and i not in res:
                res.append(i)
            for num in G[i]:
                if num not in res:
                    res.append(num)
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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def intArrayToString(data):
    if len(data) <= 0:
        return "[]"
    resStr = "[" + str(data[0])
    for i in range(1, len(data)):
        resStr += ", " + str(data[i])
    resStr += "]"

    return resStr

def intintArrayToString(data):
    if len(data) <= 0:
        return "[]"

    resStr = "[\n" + "  " + intArrayToString(data[0]) + "\n"
    for i in range(1, len(data)):
        resStr += ", " + intArrayToString(data[i]) + "\n"
    resStr += "]"

    return resStr


def loop_main(temp):
    if "],[[" in temp:
        flds = temp.replace(", ", ",").split("],[[")
    else:
        flds = temp.replace(", ", ",").split("],[")

    numCourses = int(flds[0].replace("[", ""))

    if len(flds) > 1:
        if "]]]" in flds[1]:
            flds[1] = flds[1].replace("]]]", "")
        else:
            flds[1] = flds[1].replace("]]", "")

        if len(flds[1]) > 0:
            dataStr = flds[1].split("],[")
            prerequisites = [[int(n) for n in data.split(",") ] for data in dataStr]
        else:
            prerequisites = []

    print("numCourses = {0:d}".format(numCourses))
    print("prerequisites = {0}".format(intintArrayToString(prerequisites)))

    time0 = time.time()

    sl = Solution()
    result = sl.findOrder(numCourses, prerequisites)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
