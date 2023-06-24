package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumSubsequenceCount(text string, pattern string) int64 {
	// 10ms
	var res, cnt1, cnt2 int64
	for _, ch := range []byte(text) {
		if ch == pattern[1] {
			res += cnt1
			cnt2 += 1
		}
		if ch == pattern[0] {
			cnt1 += 1
		}
	}
	return res + myMax(cnt1, cnt2)
}

func myMax(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	texts, pattern := flds[0], flds[1]
	fmt.Printf("texts = \"%s\", pattern = \"%s\"\n", texts, pattern)

	timeStart := time.Now()

	result := maximumSubsequenceCount(texts, pattern)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
