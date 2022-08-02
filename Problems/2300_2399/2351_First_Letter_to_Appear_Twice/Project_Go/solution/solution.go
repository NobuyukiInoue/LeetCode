package solution

import (
	"fmt"
	"strings"
	"time"
)

func repeatedCharacter(s string) byte {
	// 0ms
	var dic [26]int
	for _, ch := range s {
		if dic[ch-'a'] == 1 {
			return byte(ch)
		}
		dic[ch-'a']++
	}
	return '0'
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := repeatedCharacter(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%c\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
