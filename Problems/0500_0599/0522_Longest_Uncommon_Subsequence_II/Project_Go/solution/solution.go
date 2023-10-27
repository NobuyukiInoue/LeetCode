package solution

import (
	"fmt"
	"strings"
	"time"
)

func findLUSlength(strs []string) int {
	// 0ms - 2ms
	len_strs := len(strs)
	maxlen := -1
	for i := 0; i < len_strs; i++ {
		count := 0
		for j := 0; j < len_strs; j++ {
			if i != j {
				if !isSubSequence(strs[i], strs[j]) {
					count++
				} else {
					break
				}
			}
		}
		if count == len_strs-1 {
			maxlen = myMax(maxlen, len(strs[i]))
		}
	}
	return maxlen

}

func isSubSequence(a, b string) bool {
	i := 0
	for j := 0; i < len(a) && j < len(b); j++ {
		if a[i] == b[j] {
			i++
		}
	}
	return i == len(a)
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	strs := strings.Split(temp, ",")
	fmt.Printf("strs = [%s]\n", StringArrayToString(strs))

	timeStart := time.Now()

	result := findLUSlength(strs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
