package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canMakeSquare(grid [][]byte) bool {
	// 0ms
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			if isPossible(grid, i, j) {
				return true
			}
		}
	}
	return false
}

func isPossible(grid [][]byte, i, j int) bool {
	cnt_w, cnt_b := 0, 0
	for x := i; x < i+2; x++ {
		for y := j; y < j+2; y++ {
			if grid[x][y] == 'W' {
				cnt_w++
			} else {
				cnt_b++
			}
		}
	}
	if cnt_w > 2 || cnt_b > 2 {
		return true
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	grid := make([][]byte, len(flds))
	for i, _ := range flds {
		grid[i] = StringToByteArray(strings.Replace(flds[i], ",", "", -1))
	}

	fmt.Printf("grid = %s\n", ByteByteArrayToString(grid))

	timeStart := time.Now()

	result := canMakeSquare(grid)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
