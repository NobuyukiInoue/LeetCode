package main

import (
	"fmt"
	"strings"
	"time"
	"unsafe"
)

func numRookCaptures(board [][]byte) int {
	x0, y0 := 0, 0
	for i := 0; i < 8; i++ {
		for j := 0; j < 8; j++ {
			if board[i][j] == 'R' {
				x0, y0 = i, j
			}
		}
	}
	res := 0
	data := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	for _, val := range data {
		x := x0 + val[0]
		y := y0 + val[1]
		for 0 <= x && x < 8 && 0 <= y && y < 8 {
			if board[x][y] == 'p' {
				res++
			}
			if board[x][y] != '.' {
				break
			}
			x += val[0]
			y += val[1]
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	board := make([][]byte, 8)
	for i, _ := range board {
		rowStr := strings.Replace(flds[i], ",", "", -1)
		board[i] = *(*[]byte)(unsafe.Pointer(&rowStr))
	}

	fmt.Printf("board = \n")
	for _, data := range board {
		fmt.Printf("%s\n", data)
	}

	timeStart := time.Now()

	result := numRookCaptures(board)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
