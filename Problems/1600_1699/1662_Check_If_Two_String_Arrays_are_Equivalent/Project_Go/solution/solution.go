package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	// 0ms
	return strings.Join(word1[:], "") == strings.Join(word2[:], "")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	word1 := strings.Split(flds[0], ",")
	word2 := strings.Split(flds[1], ",")
	fmt.Printf("word1 = [%s]\n", StringArrayToString(word1))
	fmt.Printf("word2 = [%s]\n", StringArrayToString(word2))

	timeStart := time.Now()

	result := arrayStringsAreEqual(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
