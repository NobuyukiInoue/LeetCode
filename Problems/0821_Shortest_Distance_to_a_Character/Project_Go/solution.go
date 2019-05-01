package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func shortestToChar(S string, C byte) []int {
	n := len(S)
	pos := -n
	ans := make([]int, len(S))
	for i := 0; i < n; i++ {
		if S[i] == C {
			pos = i
		}
		ans[i] = i - pos
	}
	for i := n - 1; i >= 0; i-- {
		if S[i] == C {
			pos = i
		}
		ans[i] = min(ans[i], abs(i-pos))
	}
	return ans
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	words := strings.Split(temp, "],[")
	S := words[0]
	C := words[1][0]

	fmt.Printf("S = %s, C = %c\n", S, C)

	timeStart := time.Now()

	result := shortestToChar(S, C)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArray2string(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
