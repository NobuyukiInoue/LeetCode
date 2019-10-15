package solution

import (
	"fmt"
	"strings"
	"time"
)

func uncommonFromSentences(A string, B string) []string {
	allString := append(strings.Split(A, " "), strings.Split(B, " ")...)
	ans := allString[:0]
	var mp = make(map[string]int)

	for _, v := range allString {
		if k, ok := mp[v]; ok {
			k++
			mp[v] = k
		} else {
			mp[v] = 1
		}
	}
	for k, v := range mp {
		if v == 1 {
			ans = append(ans, k)
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	words := strings.Split(temp, "],[")

	A := words[0]
	B := words[1]
	fmt.Printf("A = %s, B = %s\n", A, B)

	timeStart := time.Now()

	result := uncommonFromSentences(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
