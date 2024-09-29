package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func maximumTotalSum(maximumHeight []int) int64 {
	// 243ms - 251ms
	sort.Sort(sort.IntSlice(maximumHeight))
	n := len(maximumHeight)
	cur := int64(maximumHeight[n-1])
	ans := int64(0)
	for i := n - 1; i >= 0; i-- {
		cur = myMin(cur, int64(maximumHeight[i]))
		if cur <= 0 {
			return -1
		}
		ans += cur
		cur--
	}
	return ans
}

func myMin(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	maximumHeight := StringToIntArray(flds)
	fmt.Printf("maximumHeight = [%s]\n", IntArrayToString(maximumHeight))

	timeStart := time.Now()

	result := maximumTotalSum(maximumHeight)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
