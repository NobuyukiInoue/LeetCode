package solution

import (
	"fmt"
	"strings"
	"time"
)

var mapping = map[byte]string {
	'1': "",
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
	'0': " ",
}

func letterCombinations(digits string) []string {
	// 0ms
	ans := []string{}

	if len(digits) == 0 {
		return ans
	}

	helper(digits, 0, "", &ans)

	return ans
}

func helper(digits string, pos int, s string, strs *[]string) {
	if pos == len(digits) {
		*strs = append(*strs, s)
		return
	}
	
	for _, c := range mapping[digits[pos]] {
		helper(digits, pos + 1, s + string(c), strs)
	}
	return
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	digits := strings.Replace(temp, "]", "", -1)
	fmt.Printf("digits = \"%s\"\n", digits)

	timeStart := time.Now()

	result := letterCombinations(digits)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
