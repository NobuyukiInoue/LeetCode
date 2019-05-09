package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func calPoints(ops []string) int {
	var ans []int
	cn := 0
	for _, v := range ops {
		switch {
		case v == "+":
			ans = append(ans, ans[len(ans)-1]+ans[len(ans)-2])
		case v == "C":
			ans = ans[:len(ans)-1]
		case v == "D":
			ans = append(ans, ans[len(ans)-1]*2)
		default:
			point, _ := strconv.Atoi(v)
			ans = append(ans, point)
		}
	}
	for _, v := range ans {
		cn = cn + v
	}
	return cn
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	ops := strings.Split(temp, ",")

	fmt.Printf("ops = %s\n", ops)

	timeStart := time.Now()

	result := calPoints(ops)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
