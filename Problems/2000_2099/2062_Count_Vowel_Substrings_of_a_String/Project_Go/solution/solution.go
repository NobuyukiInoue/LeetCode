package solution

import (
	"fmt"
	"strings"
	"time"
)

func countVowelSubstrings(word string) int {
	// 0ms
	count := 0
loop:
	for m := 0; m < len(word); m++ {
		a, e, i, o, u := 0, 0, 0, 0, 0
		for n := m; n < len(word); n++ {
			switch word[n] {
			case 'a':
				a++
			case 'e':
				e++
			case 'i':
				i++
			case 'o':
				o++
			case 'u':
				u++
			default:
				continue loop
			}
			if a > 0 && e > 0 && i > 0 && o > 0 && u > 0 {
				count++
			}
		}
	}
	return count
}

/*
func countVowelSubstrings2(word string) int {
	// 0ms
	start, end, count := 0, 0, 0
	vowel := map[byte]int{}
	for start < len(word) {
		for start < len(word) && !isVowel(word[start]) {
			start++
		}
		end = start
		for end < len(word) && isVowel(word[end]) {
			vowel[word[end]] = end
			if len(vowel) == 5 {
				temp := myCount(start, &vowel)
				count += temp
			}
			end++
		}
		vowel = map[byte]int{}
		start = end + 1
	}
	return count
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func myCount(s int, myMap *map[byte]int) int {
	last := math.MaxInt64
	for _, val := range *myMap {
		last = myMin(last, val)
	}
	return last - s + 1
}

func isVowel(c byte) bool {
	if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
		return true
	}
	return false
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := countVowelSubstrings(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
