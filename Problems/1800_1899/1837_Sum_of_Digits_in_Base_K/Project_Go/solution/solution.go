package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumBase(n int, k int) int {
	// 0ms
	num := 0
	for n > 0 {
		num += n % k
		n /= k
	}
	return num
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, k = %d\n", n, k)

	timeStart := time.Now()

	result := sumBase(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
