package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func maxCoins_asc(piles []int) int {
	// 119ms - 126ms
	sort.Sort(sort.IntSlice(piles))
	ans, n := 0, len(piles)
	for i := n - 2; i >= n/3; i -= 2 {
		ans += piles[i]
	}
	return ans
}

func maxCoins2(piles []int) int {
	// 124ms - 134ms
	sort.Sort(sort.Reverse(sort.IntSlice(piles)))
	ans := 0
	for i := 1; i < len(piles)*2/3; i += 2 {
		ans += piles[i]
	}
	return ans
}

func maxCoins(piles []int) int {
	// 108ms - 149ms
	sort.Slice(piles, func(i, j int) bool { return piles[i] > piles[j] })
	ans := 0
	for i := 1; i < len(piles)*2/3; i += 2 {
		ans += piles[i]
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	piles := StringToIntArray(flds)
	fmt.Printf("piles = [%s]\n", IntArrayToString(piles))

	timeStart := time.Now()

	result := maxCoins(piles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
