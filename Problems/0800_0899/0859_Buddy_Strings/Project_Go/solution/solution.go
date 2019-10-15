package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func buddyStrings(A string, B string) bool {
	if len(A) != len(B) {
		return false
	}
	if len(A) < 2 {
		return false
	}

	mismatch_count := 0
	var mis_letter1, mis_letter2 byte
	switched := false

	for i := 0; i < len(A); i++ {
		if A[i] != B[i] {
			if switched {
				return false
			} else if mismatch_count > 0 {
				if mis_letter1 == B[i] && mis_letter2 == A[i] {
					switched = true
				} else {
					return false
				}
			} else {
				mismatch_count++
				mis_letter1 = A[i]
				mis_letter2 = B[i]
			}
		}
	}

	if !switched {
		if strings.Compare(A, B) == 0 {
			letter_count := make(map[rune]int)
			for _, c := range A {
				letter_count[c]++
				if letter_count[c] > 1 {
					return true
				}
			}
			return false
		} else {
			return false
		}
	}
	return true
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

	result := buddyStrings(A, B)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
