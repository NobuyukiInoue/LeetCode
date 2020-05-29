package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maxVowels(s string, k int) int {
	// 4ms
	count := 0
	for i := 0; i < k; i++ {
		if i >= len(s) {
			break
		}
		if isVowel(s[i]) {
			count++
		}
	}

	maxCount := count
	for i := k; i < len(s); i++ {
		if isVowel(s[i-k]) {
			count--
		}
		if isVowel(s[i]) {
			count++
		}
		if count > maxCount {
			maxCount = count
		}
	}

	return maxCount
}

func isVowel(c byte) bool {
	if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
		return true
	}
	return false
}

func maxVowels2(s string, k int) int {
	// 16ms
	count := 0
	targetChars := "aeiou"
	for i := 0; i < k; i++ {
		if i >= len(s) {
			break
		}
		if strings.Index(targetChars, string(s[i])) >= 0 {
			count++
		}
	}

	maxCount := count
	for i := k; i < len(s); i++ {
		if strings.Index(targetChars, string(s[i-k])) >= 0 {
			count--
		}
		if strings.Index(targetChars, string(s[i])) >= 0 {
			count++
		}
		if count > maxCount {
			maxCount = count
		}
	}

	return maxCount
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := maxVowels(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
