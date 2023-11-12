package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distributeCandies(n int, limit int) int {
	// 0ms
	ans := 0
	for i := 0; i < myMin(n, limit)+1; i++ {
		ans += helper(n-i, limit)
	}
	return ans
}

func helper(n, limit int) int {
	min_v := myMax(0, n-limit)
	max_v := myMin(n, limit)
	return myMax(0, max_v-min_v+1)
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	limit, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, limit = %d\n", n, limit)

	timeStart := time.Now()

	result := distributeCandies(n, limit)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
