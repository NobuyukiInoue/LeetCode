package solution

import (
	"fmt"
	"strings"
	"time"
)

func makeSmallestPalindrome(s string) string {
	// 24ms - 28ms
	arr_s := []rune(s)
	left, right := 0, len(s)-1
	for left < right {
		if arr_s[left] < arr_s[right] {
			arr_s[right] = arr_s[left]
		} else if arr_s[left] > arr_s[right] {
			arr_s[left] = arr_s[right]
		}
		left++
		right--
	}
	return string(arr_s)
}

func makeSmallestPalindrome2(s string) string {
	// 29ms - 30ms
	arr_s := []byte(s)
	for left, right := 0, len(s)-1; left < right; left, right = left+1, right-1 {
		if arr_s[left] < arr_s[right] {
			arr_s[right] = arr_s[left]
		} else if arr_s[left] > arr_s[right] {
			arr_s[left] = arr_s[right]
		}
	}
	return string(arr_s)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := makeSmallestPalindrome(s)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
