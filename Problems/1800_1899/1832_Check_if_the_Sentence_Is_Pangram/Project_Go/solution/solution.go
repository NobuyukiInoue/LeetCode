package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkIfPangram(sentence string) bool {
	// 0ms
	cnts := make(map[rune]int, 0)
	count := 0
	for _, ch := range sentence {
		if cnts[ch] == 0 {
			cnts[ch]++
			count++
			if count >= 26 {
				return true
			}
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	sentence := strings.Replace(temp, "]", "", -1)
	fmt.Printf("sentence = %s\n", sentence)

	timeStart := time.Now()

	result := checkIfPangram(sentence)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
