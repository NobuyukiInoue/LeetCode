package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func updateBoard(board [][]byte, click []int) [][]byte {
	// 32ms
	m, n := len(board), len(board[0])
	row, col := click[0], click[1]

	if board[row][col] == 'M' {
		board[row][col] = 'X'
	} else {
		count := 0
		for i := -1; i < 2; i++ {
			for j := -1; j < 2; j++ {
				if i == 0 && j == 0 {
					continue
				}
				r, c := row+i, col+j
				if r < 0 || r >= m || c < 0 || c >= n {
					continue
				}
				if board[r][c] == 'M' || board[r][c] == 'X' {
					count++
				}
			}
		}

		if count > 0 {
			board[row][col] = (byte)(count + '0')
		} else {
			board[row][col] = 'B'
			for i := -1; i < 2; i++ {
				for j := -1; j < 2; j++ {
					if i == 0 && j == 0 {
						continue
					}
					r, c := row+i, col+j
					if r < 0 || r >= m || c < 0 || c >= n {
						continue
					}
					if board[r][c] == 'E' {
						updateBoard(board, []int{r, c})
					}
				}
			}
		}
	}
	return board
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\",\"", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")
	fld0 := strings.Split(flds[0], "],[")
	board := make([][]byte, len(fld0))
	for i := 0; i < len(fld0); i++ {
		board[i] = StringToByteArray(fld0[i])
	}
	fmt.Printf("board = %s\n", ByteByteArrayToGridString(board))
	fld1 := strings.Split(flds[1], ",")
	click := make([]int, 2)
	for i := 0; i < len(fld1); i++ {
		click[i], _ = strconv.Atoi(fld1[i])
	}

	timeStart := time.Now()

	result := updateBoard(board, click)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ByteByteArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
