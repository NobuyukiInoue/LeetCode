package solution

import (
	"fmt"
	"strings"
	"time"
)

func nextGreatestLetter(letters []byte, target byte) byte {
	if len(letters) <= 0 {
		return 'a'
	}

	l := 0
	r := len(letters) - 1

	for l < r-1 {
		mid := (l + r) / 2
		if letters[mid] <= target {
			l = mid + 1
		} else {
			r = mid
		}
	}

	if letters[l] > target {
		return letters[l]
	} else if letters[r] > target {
		return letters[r]
	} else {
		return letters[0]
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")

	letters := make([]byte, len(words))
	for i := 0; i < len(words); i++ {
		letters[i] = words[i][0]
	}

	target := flds[1][0]

	fmt.Printf("letters = %s\n", letters)
	fmt.Printf("tareget = %c\n", target)

	timeStart := time.Now()

	result := nextGreatestLetter(letters, target)
	fmt.Printf("result = %c\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
