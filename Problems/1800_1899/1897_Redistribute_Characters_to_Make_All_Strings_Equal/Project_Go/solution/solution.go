package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func makeEqual(words []string) bool {
	// 0ms
	chars := make([]int, 26)
	for i := 0; i < len(chars); i++ {
		chars[i] = 0
	}

	for _, word := range words {
		for _, ch := range word {
			chars[ch-'a']++
		}
	}
	for i := 0; i < len(chars); i++ {
		if chars[i]%len(words) != 0 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := makeEqual(words)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
