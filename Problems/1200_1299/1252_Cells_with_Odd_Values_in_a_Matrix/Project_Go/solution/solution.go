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

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
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
		indices[i] = strToIntArray(data[i])
	}

	fmt.Printf("indices = [")
	for i, _ := range indices {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(indices[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(indices[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := oddCells(n, m, indices)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
