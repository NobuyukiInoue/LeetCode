package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func prisonAfterNDays(cells []int, N int) []int {
	// 0ms
	cellsLength := len(cells)
	f_cells := make([]int, cellsLength)
	next_cells := make([]int, cellsLength)

	for cycle := 0; N > 0; cycle++ {
		N--
		for i := 1; i < cellsLength - 1; i++ {
			if cells[i - 1] == cells[i + 1] {
				next_cells[i] = 1
			} else {
				next_cells[i] = 0
			}
		}
		if cycle == 0 {
			copy(f_cells, next_cells)
		} else if compareSameLengthArrays(next_cells, f_cells) {
			N %= cycle
		}
		copy(cells, next_cells)
	}

	return cells
}

func compareSameLengthArrays(a []int, b []int) bool {
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[")

	cells := StringToIntArray(strings.Replace(flds[0], "[[", "", -1))
	N, _ := strconv.Atoi(strings.Replace(flds[1], "]]", "", -1 ))
	fmt.Printf("cells = [%s], N = %d\n", IntArrayToString(cells), N)

	timeStart := time.Now()

	result := prisonAfterNDays(cells, N)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
