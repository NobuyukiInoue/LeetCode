package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func binaryGap(N int) int {
	res, d := 0, -32
	for ; N > 0; N /= 2 {
		if N%2 == 1 {
			res = max(res, d)
			d = 0
		}
		d++
	}
	return res
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	N, _ := strconv.Atoi(flds)

	fmt.Printf("N = %d\n", N)

	timeStart := time.Now()

	result := binaryGap(N)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
