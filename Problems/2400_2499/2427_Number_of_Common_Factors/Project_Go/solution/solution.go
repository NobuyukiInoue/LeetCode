package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func commonFactors(a int, b int) int {
	// 0ms
	ans := 0
	for i := 1; i < myMin(a, b)+1; i++ {
		if a%i == 0 && b%i == 0 {
			ans++
		}
	}
	return ans
}

func myMin(a int, b int) int {
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
	a, _ := strconv.Atoi(flds[0])
	b, _ := strconv.Atoi(flds[1])
	fmt.Printf("a = %d, b = %d\n", a, b)

	timeStart := time.Now()

	result := commonFactors(a, b)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
