package solution

import (
	"fmt"
	"strings"
	"time"
)

func strStr(haystack string, needle string) int {
	// 2ms
	for i := 0; i <= len(haystack)-len(needle); i++ {
		if haystack[i] == needle[0] {
			isSame := true
			for j := 1; j < len(needle); j++ {
				if haystack[i+j] != needle[j] {
					isSame = false
					break
				}
			}
			if isSame {
				return i
			}
		}
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	haystack, needle := flds[0], flds[1]
	fmt.Printf("haystack = %s, needle = %s\n", haystack, needle)

	timeStart := time.Now()

	result := strStr(haystack, needle)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
