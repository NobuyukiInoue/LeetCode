package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func maxCount(m int, n int, ops [][]int) int {
	if ops == nil || len(ops) == 0 {
		return m * n
	}

	row := math.MaxInt32
	col := math.MaxInt32

	for _, op := range ops {
		row = IntMin(row, op[0])
		col = IntMin(col, op[1])
	}

	return row * col
}

func IntMin(a int, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	m_and_n := strings.Split(flds[0], "],[")
	m, _ := strconv.Atoi(m_and_n[0])
	n, _ := strconv.Atoi(m_and_n[1])
	fmt.Printf("m = %d, n = %d\n", m, n)

	nums := strings.Split(flds[1], "],[")
	var ops [][]int
	if len(nums[0]) == 0 {
		ops = make([][]int, 0)
	} else {
		ops = make([][]int, len(nums))
		for i, _ := range nums {
			ops[i] = StringToIntArray(nums[i])
		}
	}
	fmt.Printf("ops = %s\n", IntIntArrayToString(ops))

	timeStart := time.Now()

	result := maxCount(m, n, ops)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
