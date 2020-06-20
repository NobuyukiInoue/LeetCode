package solution

import (
	"fmt"
	"strings"
	"time"
)

func gameOfLife(board [][]int) {
	// 0ms
	if board == nil || len(board) == 0 {
		return
	}

	m, n := len(board), len(board[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			lives := liveNeighbors(board, i, j, m, n)

			if board[i][j] == 1 && lives >= 2 && lives <= 3 {
				board[i][j] = 3
			}
			if board[i][j] == 0 && lives == 3 {
				board[i][j] = 2
			}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			board[i][j] >>= 1
		}
	}

	printBoard(board)
}

func liveNeighbors(board [][]int, i int, j int, m int, n int) int {
	lives := 0
	for x := myMax(i-1, 0); x <= myMin(i+1, m-1); x++ {
		for y := myMax(j-1, 0); y <= myMin(j+1, n-1); y++ {
			lives += board[x][y] & 1
		}
	}
	lives -= board[i][j] & 1

	return lives
}

func myMax(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}

func myMin(a int, b int) int {
	if a <= b {
		return a
	}
	return b
}

func printBoard(board [][]int) {
	fmt.Printf("board = [\n")
	for i, _ := range board {
		if i == 0 {
			fmt.Printf(" [%s]\n", IntArrayToString(board[i]))
		} else {
			fmt.Printf(",[%s]\n", IntArrayToString(board[i]))
		}
	}
	fmt.Printf("]\n")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	board := make([][]int, len(flds))
	for i := 0; i < len(board); i++ {
		board[i] = StringToIntArray(flds[i])
	}
	printBoard(board)

	timeStart := time.Now()

	gameOfLife(board)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
