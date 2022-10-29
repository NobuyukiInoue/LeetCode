package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func equalFrequency(word string) bool {
	// 0ms
	freq := make([]int, 26)
	for _, ch := range word {
		freq[ch-'a']++
	}
	for _, ch := range word {
		freq[ch-'a']--
		if checkAllSame(freq) {
			return true
		}
		freq[ch-'a']++
	}
	return false
}

func checkAllSame(freq []int) bool {
	i := 0
	same := 0
	for i = 0; i < len(freq); i++ {
		if freq[i] > 0 {
			same = freq[i]
			break
		}
	}
	for j := i + 1; j < len(freq); j++ {
		if freq[j] > 0 && freq[j] != same {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := equalFrequency(word)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
