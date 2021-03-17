package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func countArrangement(n int) int {
	// 44ms
	memo := make([]int, 1 << uint64(n) - 1)
	return dfs(memo, n, 1, 0)
}

func dfs(memo []int, n int, pos int, used int) int {
	if bitCount(used) == n {
		return 1
	}

	if memo[used] > 0 {
		return memo[used]
	}

	res := 0
	for i := 1; i <= n; i++ {
		if i % pos != 0 && pos % i != 0 {
			continue
		}
		mask := 1 << (uint64(i) - 1)
		if (used & mask) == 0 {
			res += dfs(memo, n, pos + 1, used | mask)
		}
	}

	memo[used] = res
	return res
}

func bitCount(i int) int {
	i = i - ((i >> 1) & 0x55555555)
	i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
	i = (i + (i >> 4)) & 0x0f0f0f0f
	i = i + (i >> 8)
	i = i + (i >> 16)
	return i & 0x3f
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(flds)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := countArrangement(n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
