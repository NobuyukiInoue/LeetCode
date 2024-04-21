package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxScoreSightseeingPair(values []int) int {
	// 37ms - 39ms
	ans, prev := 0, values[0]
	for i := 1; i < len(values); i++ {
		ans = myMax(ans, values[i]-i+prev)
		prev = myMax(prev, values[i]+i)
	}
	return ans
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	values := StringToIntArray(flds)
	fmt.Printf("values = [%s]\n", IntArrayToString(values))

	timeStart := time.Now()

	result := maxScoreSightseeingPair(values)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
