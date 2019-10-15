package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func detectCapitalUse(word string) bool {
	left := word[1:]
	if 'a' <= word[0] && word[0] <= 'z' {
		return !isNotAllLower(left)
	} else {
		return !(isNotAllLower(left) && isNotAllUpper(left))
	}
}

func isNotAllLower(str string) bool {
	for i := 0; i < len(str); i++ {
		if 'A' <= str[i] && str[i] <= 'Z' {
			return true
		}
	}
	return false
}

func isNotAllUpper(str string) bool {
	for i := 0; i < len(str); i++ {
		if 'a' <= str[i] && str[i] <= 'z' {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)

	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := detectCapitalUse(word)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
