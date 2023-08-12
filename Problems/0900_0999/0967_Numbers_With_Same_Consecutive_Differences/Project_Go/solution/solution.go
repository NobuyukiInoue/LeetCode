package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// 2ms
var res []int
var K int

func numsSameConsecDiff(n int, k int) []int {
	res = make([]int, 0)
	K = k
	for i := 1; i <= 9; i++ {
		df(i, n-1, i)
	}
	return res
}

func df(i int, n int, val int) {
	if n == 0 {
		res = append(res, val)
		return
	}
	if i-K >= 0 {
		df(i-K, n-1, val*10+i-K)
	}
	if K != 0 && i+K <= 9 {
		df(i+K, n-1, val*10+i+K)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, k = %d\n", n, k)

	timeStart := time.Now()

	result := numsSameConsecDiff(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
