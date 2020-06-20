package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLucky(arr []int) int {
	// 4ms
	freq := make(map[int]int, 0)
	for _, v := range arr {
		value, exists := freq[v]
		if exists {
			freq[v] = value + 1
		} else {
			freq[v] = 1
		}
	}

	ans := -1
	for k, v := range freq {
		if k == v {
			ans = myMax(ans, k)
		}
	}
	return ans
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := findLucky(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
