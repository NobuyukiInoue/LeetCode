package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func tribonacci(n int) int {
	if n < 1 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	t0, t1, t2 := 0, 1, 1
	for i := 3; i <= n; i++ {
		t0, t1, t2 = t1, t2, t0+t1+t2
	}
	return t2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := tribonacci(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
