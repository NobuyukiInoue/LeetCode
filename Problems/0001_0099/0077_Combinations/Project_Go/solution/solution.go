package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func combine(n int, k int) [][]int {
	// 8ms
	ans := make([][]int, 0)
	stack := make([]int, 0)
	x := 1
	for {
		stackLength := len(stack)
		if stackLength == k {
			ans = append(ans, append([]int{}, stack...))
		}
		if stackLength == k || x > n-k+stackLength+1 {
			if stackLength == 0 {
				return ans
			}
			x = stack[stackLength-1] + 1
			stack = stack[:stackLength-1]
		} else {
			stack = append(stack, x)
			x++
		}
	}
}

func combine2(n int, k int) [][]int {
	// 52ms
	ans := make([][]int, 0)
	dfs(n, k, make([]int, 0), 0, 1, &ans)
	return ans
}

func dfs(n int, count int, cur []int, i, j int, ans *[][]int) {
	if i == count {
		*ans = append(*ans, append([]int{}, cur...))
	}
	for x := j; x <= n; x++ {
		dfs(n, count, append(cur, x), i+1, x+1, ans)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	n, _ := strconv.Atoi(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, k = %d\n", n, k)

	timeStart := time.Now()

	result := combine(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
