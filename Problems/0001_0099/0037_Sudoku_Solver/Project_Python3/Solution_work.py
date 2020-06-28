class Solution_work:
#   def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku_work(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            fail = False
            count, pos = 0, -1
            dic = {}
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    count += 1
                if not board[i][j] in dic:
                    dic[board[i][j]] = 1
                    if board[i][j] == ".":
                        pos = j
                elif count > 1:
                    fail = True
                    break
            if fail:
                continue
            if not "." in dic:
                continue
            for n in range(0, 9):
                if not n in dic:
                    board[i][pos] = n
                    break

        for j in range(len(board[0])):
            fail = False
            count, pos = 0, -1
            dic = {}
            for i in range(len(board)):
                if board[i][j] == ".":
                    count += 1
                if not board[i][j] in dic:
                    dic[board[i][j]] = 1
                    if board[i][j] == ".":
                        pos = i
                elif count > 1:
                    fail = True
                    break
            if fail:
                continue
            if not "." in dic:
                continue
            for n in range(0, 9):
                if not n in dic:
                    board[pos][j] = n
                    break

        xy = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        fail = False
        count, pos = 0, (-1, -1)
        dic = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for n in xy:
                    if board[i + n[0]][j + n[1]] == ".":
                        count += 1
                    if not board[i + n[0]][j + n[1]] in dic:
                        dic[board[i + n[0]][j + n[1]]] = 1
                        if board[i + n[0]][j + n[1]] == ".":
                            pos = (i + n[0], j + n[1])
                    elif count > 1:
                        fail = True
                        break
            if fail:
                continue
            if not "." in dic:
                continue
            for n in range(0, 9):
                if dic[n] == 0:
                    board[pos[0], pos[1]] = n

        print("board = ")
        for i in range(0, len(board)):
            print("{0}".format(board[i]))

        return
