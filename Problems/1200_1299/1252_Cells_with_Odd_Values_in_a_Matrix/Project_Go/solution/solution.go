package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func oddCells(n int, m int, indices [][]int) int {
	// 0ms
	row, col := make([]int, n), make([]int, m)
	for _, idx := range indices {
		row[idx[0]] ^= 1
		col[idx[1]] ^= 1
	}
	cnt := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if row[i]^col[j] == 1 {
				cnt++
			}
		}
	}
	return cnt
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	s := strings.Replace(flds[0], "[[", "", -1)
	fld0 := strings.Split(s, ",")
	n, _ := strconv.Atoi(fld0[0])
	m, _ := strconv.Atoi(fld0[1])
	fmt.Printf("n = %d, m = %d\n", n, m)

	data := strings.Split(flds[1], "],[")

	indices := make([][]int, len(data))
	for i := 0; i < len(data); i++ {
		indices[i] = StringToIntArray(data[i])
	}
	fmt.Printf("indices = %s\n",IntIntArrayToString(indices))

	timeStart := time.Now()

	result := oddCells(n, m, indices)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
