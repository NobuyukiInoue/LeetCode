package solution

import (
	"fmt"
	"strings"
	"time"
)

func largestMerge(word1 string, word2 string) string {
	// 7ms - 8ms
	index1, index2 := 0, 0
	ans := make([]byte, 0, len(word1)+len(word2))
	for len(ans) != cap(ans) {
		if word1[index1:] > word2[index2:] {
			ans = append(ans, word1[index1])
			index1++
		} else {
			ans = append(ans, word2[index2])
			index2++
		}
	}
	return string(ans)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	word1, word2 := flds[0], flds[1]
	fmt.Printf("word1 = \"%s\", word2 = \"%s\"\n", word1, word2)

	timeStart := time.Now()

	result := largestMerge(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
