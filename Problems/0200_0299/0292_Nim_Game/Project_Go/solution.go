package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canWinNim(n int) bool {
	return !(n%4 == 0)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(temp)

	timeStart := time.Now()

	result := canWinNim(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
