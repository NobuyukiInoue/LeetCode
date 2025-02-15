package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func smallestNumber(n int, t int) int {
	// 0ms
	for ; getProd(n)%t != 0; n++ {
	}
	return n
}

func getProd(n int) int {
	prod := 1
	for n > 0 {
		prod *= n % 10
		n /= 10
	}
	return prod
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	t, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, t = %d\n", n, t)

	timeStart := time.Now()

	result := smallestNumber(n, t)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
