package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func differenceOfSums(n int, m int) int {
	// 0ms
	return (1+n)*n/2 - (1+n/m)*(n/m)*m
}

func differenceOfSums2(n int, m int) int {
	// 0ms - 4ms
	num1, num2 := 0, 0
	for i := 1; i < n+1; i++ {
		if i%m != 0 {
			num1 += i
		} else {
			num2 += i
		}
	}
	return num1 - num2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	m, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, m = %d\n", n, m)

	timeStart := time.Now()

	result := differenceOfSums(n, m)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
