package solution

import (
	"fmt"
	"strings"
	"time"
)

func countBattleships(board [][]byte) int {
	// 0ms
	res := 0
	for i, _ := range(board) {
		for j, _ := range(board[i]) {
			if board[i][j] == 'X' {
				if i > 0 && board[i - 1][j] == 'X' || j > 0 && board[i][j - 1] == 'X' {
					continue
				}
				res++
			}
		}
	}
	return res
}

func searchIslands(grid [][]byte, i int, j int) {
	if grid[i][j] == '0' {
		return
	}
	grid[i][j] = '0'
	if i-1 >= 0 {
		searchIslands(grid, i-1, j)
	}
	if i+1 < len(grid) {
		searchIslands(grid, i+1, j)
	}
	if j-1 >= 0 {
		searchIslands(grid, i, j-1)
	}
	if j+1 < len(grid[i]) {
		searchIslands(grid, i, j+1)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\",\"", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	board := make([][]byte, len(flds))
	for i := 0; i < len(board); i++ {
		board[i] = StringToByteArray(flds[i])
	}
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))

	timeStart := time.Now()

	result := countBattleships(board)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
