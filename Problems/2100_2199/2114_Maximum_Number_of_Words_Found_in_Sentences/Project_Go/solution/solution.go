package solution

import (
	"fmt"
	"strings"
	"time"
)

func mostWordsFound(sentences []string) int {
	// 4ms
	res := 0
	for _, s := range sentences {
		res = myMax(res, len(strings.Split(s, " ")))
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	sentences := strings.Split(temp, ",")
	fmt.Printf("sentences = %s\n", sentences)

	timeStart := time.Now()

	result := mostWordsFound(sentences)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
