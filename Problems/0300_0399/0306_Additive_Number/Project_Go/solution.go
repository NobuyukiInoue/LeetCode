package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isAdditiveNumber(num string) bool {
	if num == "" || len(num) < 3 {
		return false
	}
	return dfs(num, 0, -1, -1)
}

func dfs(vals string, idx int, prev int, pp int) bool {
	if idx == len(vals) {
		return true
	}
	total := 0
	for i := idx; i < len(vals); i++ {
		ch := int(vals[i])
		if total == 0 && i > idx {
			break
		}
		total = total*10 + ch - int('0')
		if pp == -1 && i+1 == len(vals) {
			return false
		} else if (pp == -1 || pp+prev == total) && dfs(vals, i+1, total, prev) {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)

	fmt.Printf("num = %s\n", num)

	timeStart := time.Now()

	result := isAdditiveNumber(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
