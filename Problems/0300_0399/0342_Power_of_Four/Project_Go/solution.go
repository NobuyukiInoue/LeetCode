package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPowerOfFour(num int) bool {
	if num <= 0 {
		return false
	}

	for num != 1 {
		if num%4 != 0 {
			return false
		}
		num /= 4
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(temp)

	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := isPowerOfFour(num)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
