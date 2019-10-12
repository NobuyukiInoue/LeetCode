package main

import (
	"fmt"
	"strings"
	"time"
)

func multiply(num1 string, num2 string) string {
	// 0ms
	m, n := len(num1), len(num2)
	pos := make([]int, m+n)

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			mul := (int)((num1[i] - '0') * (num2[j] - '0'))
			p1, p2 := i+j, i+j+1
			sum := mul + pos[p2]

			pos[p1] += sum / 10
			pos[p2] = (sum) % 10
		}
	}

	sb := make([]byte, 0)
	for _, p := range pos {
		if !(len(sb) == 0 && p == 0) {
			sb = append(sb, (byte)(p+'0'))
		}
	}

	if len(sb) == 0 {
		return "0"
	}
	return string(sb)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	num1 := flds[0]
	num2 := flds[1]

	fmt.Printf("num1 = %s, num2 = %s\n", num1, num2)
	timeStart := time.Now()

	result := multiply(num1, num2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
