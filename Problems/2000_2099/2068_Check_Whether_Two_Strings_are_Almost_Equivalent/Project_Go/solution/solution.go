package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkAlmostEquivalent(word1 string, word2 string) bool {
	// 0ms
	i := len(word1)
	frequency := make([]int, 26)
	for i--; i >= 0; i-- {
		frequency[word1[i]-'a']++
		frequency[word2[i]-'a']--
	}
	for i++; i < 26; i++ {
		if frequency[i] > 3 || frequency[i] < -3 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	word1, word2 := flds[0], flds[1]
	fmt.Printf("word1 = \"%s\", word2 = \"%s\"\n", word1, word2)

	timeStart := time.Now()

	result := checkAlmostEquivalent(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
