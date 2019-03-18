package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findComplement(num int) int {
	ones := 0
	t := num
	for t > 0 {
		ones <<= 1
		ones |= 1
		t >>= 1
	}
	return ones ^ num
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := findComplement(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.Itoa(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
