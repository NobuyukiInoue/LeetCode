package solution

import (
	"fmt"
	"strings"
	"time"
)

func shortestCompletingWord(licensePlate string, words []string) string {
	freq := make([]int, 26)
	licensePlate = strings.ToLower(licensePlate)
	for _, c := range licensePlate {
		if 'a' <= c && c <= 'z' {
			freq[c-'a']++
		}
	}

	res := ""
	for _, s := range words {
		temp := make([]int, 26)
		copy(temp, freq)
		if (len(res) == 0 || len(s) < len(res)) && check(temp, s) {
			res = s
		}
	}

	return res
}

func check(freq []int, s string) bool {
	for _, c := range s {
		freq[c-'a']--
	}

	for _, f := range freq {
		if f > 0 {
			return false
		}
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	licensePlate := flds[0]
	words := strings.Split(flds[1], ",")

	fmt.Printf("licensePlate = %s\n", licensePlate)
	fmt.Printf("words[] = %s\n", words)

	timeStart := time.Now()

	result := shortestCompletingWord(licensePlate, words)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
