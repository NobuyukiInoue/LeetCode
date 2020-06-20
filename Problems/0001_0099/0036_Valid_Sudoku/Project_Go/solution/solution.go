package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
	"unsafe"
)

func isValidSudoku(board [][]byte) bool {
	rule1 := make([][]bool, 9)
	for i := 0; i < len(rule1); i++ {
		rule1[i] = make([]bool, 10)
	}
	rule2 := make([][]bool, 9)
	for i := 0; i < len(rule2); i++ {
		rule2[i] = make([]bool, 10)
	}
	rule3 := make([][]bool, 9)
	for i := 0; i < len(rule3); i++ {
		rule3[i] = make([]bool, 10)
	}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			digit := board[i][j]
			if digit != '.' {
				idx3 := (3*(int)(i/3) + (int)(j/3))
				digit -= '0'
				if rule1[j][digit] || rule2[i][digit] || rule3[idx3][digit] {
					return false
				}
				rule1[j][digit] = true
				rule2[i][digit] = true
				rule3[idx3][digit] = true
			}
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	board := make([][]byte, 9)
	for i, _ := range board {
		rowStr := strings.Replace(flds[i], ",", "", -1)
		board[i] = *(*[]byte)(unsafe.Pointer(&rowStr))
	}
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))

	timeStart := time.Now()

	result := isValidSudoku(board)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
