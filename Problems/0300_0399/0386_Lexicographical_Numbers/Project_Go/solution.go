package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func lexicalOrder(n int) []int {
	res := make([]int, 0)
	dfs(&res, n, 1)
	return res
}

func dfs(res *[]int, n int, cur int) {
	if cur > n {
		return
	}
	if len(*res) == 0 {
		*res = make([]int, 1)
		(*res)[0] = cur
	} else {
		*res = append(*res, cur)
	}
	dfs(res, n, cur*10)
	if cur%10 < 9 {
		dfs(res, n, cur+1)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := lexicalOrder(n)

	timeEnd := time.Now()

	fmt.Printf("result = [")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf(" %d", result[i])
		} else {
			fmt.Printf(", %d", result[i])
		}
	}
	fmt.Printf("]\n")

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
