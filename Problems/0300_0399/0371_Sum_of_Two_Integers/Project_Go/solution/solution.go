package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getSum(a int, b int) int {
	if a == 0 {
		return b
	}
	if b == 0 {
		return a
	}
	for b != 0 {
		temp := (a & b) << 1
		a = a ^ b
		b = temp
	}
	return a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	a, _ := strconv.Atoi(flds[0])
	b, _ := strconv.Atoi(flds[1])

	fmt.Printf("a = %d, b = %d\n", a, b)

	timeStart := time.Now()

	result := getSum(a, b)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
