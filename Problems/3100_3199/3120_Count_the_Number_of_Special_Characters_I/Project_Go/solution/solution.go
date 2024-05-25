package solution

import (
	"fmt"
	"strings"
	"time"
)

func numberOfSpecialChars(word string) int {
	// 0ms
	ans := 0
	var cnts [128]bool
	for _, ch := range word {
		cnts[ch] = true
	}
	for i := 'A'; i <= 'Z'; i++ {
		if cnts[i] && cnts[i+0x20] {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := numberOfSpecialChars(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
