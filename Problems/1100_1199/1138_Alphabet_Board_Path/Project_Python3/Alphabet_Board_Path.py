import os
import sys
import time

class Solution:
    """
    abcde
    fghij
    klmno
    pqrst
    uvwxy
    z
    """
    ##------------------------------------------------------------------------##
    ## My Solution 28ms
    ##------------------------------------------------------------------------##
    def alphabetBoardPath(self, target: str) -> str:
        # 28ms
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        res = ""
        x, y = 0, 0
        for ch in target:
            for i, _ in enumerate(board):
                pos = board[i].find(ch)
                if pos >= 0:
                    toLastRow = False
                    if x > i:
                        res += "U"*(x - i)
                    elif x < i:
                        if i == 5:
                            res += "D"*(4 - x)
                            toLastRow = True
                        else:
                            res += "D"*(i - x)
                    x = i
                    if y > pos:
                        res += "L"*(y - pos)
                    elif y < pos:
                        res += "R"*(pos - y)
                    if toLastRow:
                        res += "D"
                    res += "!"
                    y = pos
        return res

    ##------------------------------------------------------------------------##
    ## Solution2. 32ms
    ##------------------------------------------------------------------------##
    def alphabetBoardPath2(self, target: str) -> str:
        positionBoard = self.buildBoard()
        currPos = (0, 0)
        res = ""
        for nextChar in target:
            res+=self.findPath(currPos, positionBoard[nextChar])
            currPos = positionBoard[nextChar]

        return res

    def buildBoard(self):

        charDict = {}
        i, j = 0, 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            charDict[char] = (i, j)
            j+=1
            if j == 5:
                j=0
                i+=1

        return charDict

    def findPath(self, currPos, targetPos):
        path = ""

        # Handle special Z movement
        if currPos == (5, 0) and targetPos != (5, 0):
            path += "U"
            currPos = (4, 0)


        dx, dy = targetPos[1]-currPos[1], targetPos[0]-currPos[0]
        if dx >= 0:
            path += "R"*dx
        else:
            path += "L"*(-dx)

        if dy >= 0:
            path += "D"*dy
        else:
            path += "U"*(-dy)

        return path+"!"

    ##------------------------------------------------------------------------##
    ## Solution3. 632ms
    ##------------------------------------------------------------------------##
    def alphabetBoardPath3(self, target: str) -> str:
        # 632ms
        board = ["abcde","fghij","klmno","pqrst","uvwxy","z0000"] # fill "0" in blank
        res = []
        x0, y0 = 0, 0
        for s in target: #each time, find shorest path for one char
                x, y, path = self.bfs(board, x0, y0, s)
                x0, y0 = x, y # update intial index
                res.append(path)
        return "".join(res)

    # Input: initial index (indx, idy), one char (goal this time)
    # Output: index and path for the goal char
    def bfs(self, board, idx, idy, goal):
        m, n = len(board), len(board[0])
        queue = collections.deque([(idx, idy,"")])
        visited = set() # array will TLE
        dirt = {'U':(-1, 0),"D":(1,0),"L":(0, -1),"R":(0, 1)}
        while queue:
                a, b, path = queue.popleft()
                visited.add(path)
                if board[a][b] == goal:
                        return (a, b, path+"!") #return path and index
                for sign in dirt:
                        i, j = a + dirt[sign][0], b + dirt[sign][1]
                        if 0<=i<m and 0<=j<n and board[i][j]!="0" and path+sign not in visited:
                                queue.append((i, j, path+sign))
        return -1
    ##------------------------------------------------------------------------##

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
    target = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("target = {0}".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.alphabetBoardPath(target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
