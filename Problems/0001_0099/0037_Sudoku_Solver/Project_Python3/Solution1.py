class Solution:
#   def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict

        nums = [str(i) for i in range(1, 10)]
        rows, cols, cells, empty = defaultdict(set), defaultdict(set), defaultdict(set), set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.add((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    cells[i//3, j//3].add(board[i][j])

        def fill():
            i, j = max(empty, key=lambda x: len(rows[x[0]]) + len(cols[x[1]]) + len(cells[x[0]//3, x[1]//3]))
            empty.remove((i, j))
            for num in nums:
                if not (num in rows[i] or num in cols[j] or num in cells[i//3, j//3]):
                    board[i][j] = num; rows[i].add(num); cols[j].add(num); cells[i//3, j//3].add(num)
                    if not empty: return True
                    if fill(): return True
                    board[i][j] = '.'; rows[i].remove(num); cols[j].remove(num); cells[i//3, j//3].remove(num)
            empty.add((i, j))
            return False
                    
        if not empty: return 
        _ = fill()
