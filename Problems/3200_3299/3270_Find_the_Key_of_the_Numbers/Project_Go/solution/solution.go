package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func generateKey(num1 int, num2 int, num3 int) int {
	// 0ms
	ans, dv := 0, 10
	for dv < 100000 {
		d1 := num1 % dv
		d2 := num2 % dv
		d3 := num3 % dv
		ans += myMin(d1, myMin(d2, d3))
		num1 -= d1
		num2 -= d2
		num3 -= d3
		dv *= 10
	}
	return ans
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	num1, _ := strconv.Atoi(flds[0])
	num2, _ := strconv.Atoi(flds[1])
	num3, _ := strconv.Atoi(flds[2])
	fmt.Printf("num1 = %d, num2 = %d, num3 = %d\n", num1, num2, num3)

	timeStart := time.Now()

	result := generateKey(num1, num2, num3)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
