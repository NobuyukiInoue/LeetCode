package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

var visited [][]bool

func exist(board [][]byte, word string) bool {
	// 4ms
	visited = make([][]bool, len(board))
	for i := 0; i < len(visited); i++ {
		visited[i] = make([]bool, len(board[0]))
	}
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if (word[0] == board[i][j]) && search(board, word, i, j, 0) {
				return true
			}
		}
	}
	return false
}
func search(board [][]byte, word string, i int, j int, index int) bool {
	if index == len(word) {
		return true
	}
	if i >= len(board) || i < 0 || j >= len(board[i]) || j < 0 || board[i][j] != word[index] || visited[i][j] {
		return false
	}
	visited[i][j] = true
	if search(board, word, i-1, j, index+1) ||
		search(board, word, i+1, j, index+1) ||
		search(board, word, i, j-1, index+1) ||
		search(board, word, i, j+1, index+1) {
		return true
	}
	visited[i][j] = false
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	rows := strings.Split(flds[0], "],[")

	board := make([][]byte, len(rows))
	for i := 0; i < len(board); i++ {
		temp := strings.Replace(rows[i], ",", "", -1)
		board[i] = StringToByteArray(temp)
	}
	word := strings.Replace(flds[1], "]", "", -1)
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := exist(board, word)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
