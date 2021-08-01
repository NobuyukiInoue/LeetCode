package solution

import (
	"fmt"
	"strings"
	"time"
)

func canBeTypedWords(text string, brokenLetters string) int {
	// 0ms
	words := strings.Split(text, " ")
	ans := 0
	for _, word := range words {
		used := false
		for _, ch1 := range word {
			for _, ch2 := range brokenLetters {
				if ch1 == ch2 {
					used = true
					break
				}
			}
			if used {
				break
			}
		}
		if !used {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	text := flds[0]
	brokenLetters := flds[1]
	fmt.Printf("text = \"%s\", brokenLetters = \"%s\"\n", text, brokenLetters)

	timeStart := time.Now()

	result := canBeTypedWords(text, brokenLetters)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
