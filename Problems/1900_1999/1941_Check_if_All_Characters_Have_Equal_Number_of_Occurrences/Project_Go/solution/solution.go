package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func areOccurrencesEqual(s string) bool {
	// 0ms
	cnt := map[rune]int{}

	for _, ch := range s {
		cnt[ch]++
	}

	preVal := 0
	for _, v := range cnt {
		if preVal == 0 {
			preVal = v
		} else if v != preVal {
			return false
		}
	}
	return true
}

func areOccurrencesEqual2(s string) bool {
	// 0ms
	var cnt [26]int
	for _, ch := range s {
		cnt[ch-'a']++
	}

	expected := 0
	var i int
	for i = 0; i < 26; i++ {
		if cnt[i] != 0 {
			expected = cnt[i]
			break
		}
	}

	for ; i < 26; i++ {
		if cnt[i] != 0 && cnt[i] != expected {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := areOccurrencesEqual(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
