package solution

import (
	"fmt"
	"strings"
	"time"
)

func numberOfAlternatingGroups(colors []int) int {
	// 3ms
	n, ans := len(colors), 0
	for i := 0; i < n; i++ {
		var j, k int
		if i+1 < n {
			j = i + 1
		} else {
			j = i + 1 - n
		}
		if colors[i] == colors[j] {
			continue
		}
		if i+2 < n {
			k = i + 2
		} else {
			k = i + 2 - n
		}
		if colors[j] == colors[k] {
			continue
		}
		ans++
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	colors := StringToIntArray(flds)
	fmt.Printf("colors = [%s]\n", IntArrayToString(colors))

	timeStart := time.Now()

	result := numberOfAlternatingGroups(colors)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
