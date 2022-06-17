package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

// 159ms - 269ms
var counts []int
var cookies_p []int
var total int

func distributeCookies(cookies []int, k int) int {
	counts = make([]int, k)
	cookies_p = cookies
	total = math.MaxInt64
	dfs(k, 0)
	return total
}

func dfs(children int, pos int) {
	if pos >= len(cookies_p) {
		max := 0
		for _, count := range counts {
			max = myMax(max, count)
		}
		total = myMin(total, max)
		return
	}
	for i := 0; i < children; i++ {
		counts[i] += cookies_p[pos]
		dfs(children, pos+1)
		counts[i] -= cookies_p[pos]
	}
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
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
	cookies := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("cookies = [%s], k = %d\n", IntArrayToString(cookies), k)

	timeStart := time.Now()

	result := distributeCookies(cookies, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
