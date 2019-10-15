package solution

import (
	"fmt"
	"strings"
	"time"
	"unsafe"
)

var col [][]bool
var row [][]bool
var box [][]bool
var pos [][]int

func solveSudoku(board [][]byte) {
	initPosAndCheck(board)
	solve(board, 0)
}

func solve(board [][]byte, startPosIndex int) bool {
	for pi := startPosIndex; pi < len(pos); pi++ {
		i := pos[pi][0]
		j := pos[pi][1]
		if board[i][j] == '.' {
			for c := '1'; c <= '9'; c++ {
				if validPosition(i, j, c) {
					board[i][j] = string(c)[0]
					if solve(board, pi+1) {
						return true
					} else {
						board[i][j] = '.'
						num := c - '1'
						col[i][num], row[j][num], box[i/3*3+j/3][num] = false, false, false
					}
				}
			}
			return false
		}

	}
	return true
}

func validPosition(i int, j int, c rune) bool {
	num := c - '1'
	k := i/3*3 + j/3
	if col[i][num] || row[j][num] || box[k][num] {
		return false
	}
	col[i][num], row[j][num], box[k][num] = true, true, true
	return true
}

func initPosAndCheck(board [][]byte) bool {
	col = make([][]bool, 9)
	for i := 0; i < len(col); i++ {
		col[i] = make([]bool, 9)
	}
	row = make([][]bool, 9)
	for i := 0; i < len(row); i++ {
		row[i] = make([]bool, 9)
	}
	box = make([][]bool, 9)
	for i := 0; i < len(box); i++ {
		box[i] = make([]bool, 9)
	}
	pos = make([][]int, 0)

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] != '.' {
				num := board[i][j] - '1'
				col[i][num], row[j][num], box[i/3*3+j/3][num] = true, true, true
			} else {
				var temp = []int{i, j}
				pos = append(pos, temp)
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

	fmt.Printf("board = \n")
	for _, data := range board {
		fmt.Printf("%s\n", data)
	}

	timeStart := time.Now()

	solveSudoku(board)

	timeEnd := time.Now()

	fmt.Printf("board = \n")
	for _, data := range board {
		fmt.Printf("%s\n", data)
	}
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
