package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func solveNQueens(n int) [][]string {
	// 4ms
	res := make([][]string, 0)
	helper(0, make([]bool, n), make([]bool, 2*n), make([]bool, 2*n), make([]string, n), &res)
	return res
}

func helper(r int, cols []bool, d1 []bool, d2 []bool, board []string, res *[][]string) {
	boardLen := len(board)
	if r == boardLen {
		boardtemp := make([]string, boardLen)
		copy(boardtemp, board)
		*res = append(*res, boardtemp)
	} else {
		for c := 0; c < boardLen; c++ {
			id1 := r - c + boardLen
			id2 := 2*boardLen - r - c - 1
			if !cols[c] && !d1[id1] && !d2[id2] {
				row := make([]byte, boardLen)
				for i := 0; i < len(row); i++ {
					row[i] = '.'
				}
				row[c] = 'Q'
				board[r] = string(row)
				cols[c] = true
				d1[id1] = true
				d2[id2] = true
				helper(r+1, cols, d1, d2, board, res)
				cols[c] = false
				d1[id1] = false
				d2[id2] = false
			}
		}
	}
}

func str2ArrayToString(result [][]string) string {
	if len(result) <= 0 {
		return "[]"
	}

	res := ""
	for i := 0; i < len(result); i++ {
		res += "[\n"
		for j := 0; j < len(result[i]); j++ {
			if j == 0 {
				res += " [" + result[i][j] + "]\n"
			} else {
				res += ",[" + result[i][j] + "]\n"
			}
		}
		res += "]\n"
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := solveNQueens(n)

	timeEnd := time.Now()

	fmt.Printf("result =\n%s", str2ArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
