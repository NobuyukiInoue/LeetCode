package solution

import (
	"fmt"
	"strings"
	"time"
)

func lengthOfLongestSubstring(s string) int {
	length := 0
	max := 0
	start := 0

	m := map[byte]int{}
	for i := 0; i < len(s); i++ {
		if index, ok := m[s[i]]; ok {
			if index < start {
				length++
			} else {
				start = index + 1
				length = i - index
			}

		} else {
			length++
		}

		m[s[i]] = i

		if length > max {
			max = length
		}
	}

	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := lengthOfLongestSubstring(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)}
