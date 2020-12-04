package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxRepeating(sequence string, word string) int {
	// 0ms
	for i := len(sequence)/len(word); i > 0; i-- {
		if strings.Index(sequence, strings.Repeat(word, i)) >= 0 {
			return i
		}
	}
	return 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	sequence := flds[0]
	word := flds[1]
	fmt.Printf("sequence = %s\n", sequence)
	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := maxRepeating(sequence, word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
