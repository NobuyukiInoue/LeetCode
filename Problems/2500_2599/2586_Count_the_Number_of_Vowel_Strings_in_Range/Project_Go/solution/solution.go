package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
	//	"golang.org/x/exp/slices"
)

/*
func vowelStrings_use_slices(words []string, left int, right int) int {
	// go 1.18 or later.
	// go get "golang.org/x/exp/slices"
	res := 0
	vowel := []byte("aeiou")
	for i := left; i <= right; i++ {
		if slices.Contains(vowel, words[i][0]) && slices.Contains(vowel, words[i][len(words[i])-1]) {
			res++
		}
	}
	return res
}
*/

func vowelStrings(words []string, left int, right int) int {
	// 7ms
	res := 0
	vowel := "aeiou"
	for i := left; i <= right; i++ {
		if strings.Contains(vowel, string(words[i][0])) && strings.Contains(vowel, string(words[i][len(words[i])-1])) {
			res++
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	left, _ := strconv.Atoi(flds[1])
	right, _ := strconv.Atoi(flds[2])
	fmt.Printf("words = %s, left = %d, right = %d\n", StringArrayToString(words), left, right)

	timeStart := time.Now()

	result := vowelStrings(words, left, right)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
