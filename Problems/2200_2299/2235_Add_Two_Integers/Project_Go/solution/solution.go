package solution

import (
	"fmt"
	"strings"
	"time"
)

func sum(num1 int, num2 int) int {
	// 0ms - 2ms
	return num1 + num2
}

func sum2(num1 int, num2 int) int {
	// 0ms - 2ms
	var adder int
	if num2 >= 0 {
		adder = 1
	} else {
		adder = -1
		num2 = -num2
	}
	for i := 0; i < num2; i++ {
		num1 += adder
	}
	return num1
}

func sum_circuit(num1 int, num2 int) int {
	// 0ms - 2ms
	return add(num1, num2)
}

func add(x, y int) int {
	if y == 0 {
		return x
	} else if x < 0 && y < 0 {
		s := (^x) ^ (^y)
		c := ((^x) & (^y)) << 1
		return ^add(add(s, c), 1)
	}
	s := x ^ y
	c := (x & y) << 1
	return add(s, c)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	num1, num2 := nums[0], nums[1]
	fmt.Printf("num1 = %d, num2 = %d\n", num1, num2)

	timeStart := time.Now()

	result := sum(num1, num2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
