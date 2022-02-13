package solution

import (
	"fmt"
	"strings"
	"time"
)

func minDeletionSize(strs []string) int {
	// 6ms
	res, m, n := 0, len(strs[0]), len(strs)
	check := make([]int, n)
	for i, _ := range check {
		check[i] = -1
	}
	del := make([]bool, m)
	for col := 0; col < m; col++ {
		for i := 1; i < n; i++ {
			if check[i] != -1 && !del[check[i]] {
				continue
			}
			if strs[i][col] > strs[i-1][col] {
				check[i] = col
			} else if strs[i][col] < strs[i-1][col] {
				del[col] = true
				res++
				break
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	strs := strings.Split(temp, ",")
	fmt.Printf("strs = %s\n", strs)

	timeStart := time.Now()

	result := minDeletionSize(strs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
