package solution

import (
	"fmt"
	"strings"
	"time"
)

func capitalizeTitle(title string) string {
	// 0ms
	CASE_DIFF := byte('a' - 'A')
	btitle := []byte(title)
	b := 0
	for i := 0; i <= len(btitle); i++ {
		if i == len(btitle) || title[i] == ' ' {
			if i-b > 2 {
				btitle[b] -= CASE_DIFF
			}
			b = i + 1
		} else if title[i] < 'a' {
			btitle[i] += CASE_DIFF
		}
	}
	return string(btitle)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	title := strings.Replace(temp, "]", "", -1)
	fmt.Printf("title = \"%s\"\n", title)

	timeStart := time.Now()

	result := capitalizeTitle(title)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
