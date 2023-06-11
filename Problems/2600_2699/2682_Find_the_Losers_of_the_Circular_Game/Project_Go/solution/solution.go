package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func circularGameLosers(n int, k int) []int {
	// 3ms - 7ms
	check := make([]bool, n)
	var i, j, pre int
	pre = 0
	for i = 1; !check[pre]; i++ {
		check[pre] = true
		pre = (i*k + pre) % n
	}
	ans := make([]int, n-i+1)
	j = 0
	for i = 1; i < n; i++ {
		if !check[i] {
			ans[j] = i + 1
			j++
		}
	}
	return ans
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

	result := circularGameLosers(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
