package solution

import (
	"fmt"
	"strings"
	"time"
)

func solve(board [][]byte) {
	// 24ms
	m := len(board)
	if m < 1 {
		return
	}

	n := len(board[0])

	for i := 0; i < m; i++ {
		dfs1(board, m, n, i, 0)
		dfs1(board, m, n, i, n - 1)
	}

	for j := 0; j < n; j++ {
		dfs1(board, m, n, 0, j)
		dfs1(board, m, n, m - 1, j)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'O' {
				board[i][j] = 'X'
			} else if board[i][j] == 't' {
				board[i][j] = 'O'
			}
		}
	}
}

func dfs1(board [][]byte, m int, n int, i int, j int) {
	if i < 0 || j < 0 || i > m - 1 || j > n - 1 || board[i][j] != 'O' {
		return
	}

	board[i][j] = 't'
	dfs1(board, m, n, i - 1, j)
	dfs1(board, m, n, i + 1, j)
	dfs1(board, m, n, i, j - 1)
	dfs1(board, m, n, i, j + 1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_board := strings.Split(flds, "],[")
	board := make([][]byte, len(str_board))
	for i := 0; i < len(str_board); i++ {
		board[i] = StringToByteArray(str_board[i])
	}
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))

	timeStart := time.Now()

	solve(board)

	timeEnd := time.Now()

	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
