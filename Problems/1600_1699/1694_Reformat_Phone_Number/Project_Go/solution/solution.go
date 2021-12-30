package solution

import (
	"fmt"
	"strings"
	"time"
)

func reformatNumber(number string) string {
	// 0ms
	chars := []byte(number)
	cleanedChars := []byte{}

	for _, char := range chars {
		if char == ' ' || char == '-' {
			continue
		}

		cleanedChars = append(cleanedChars, char)
	}

	resultChars := []byte{}

	for i, char := range cleanedChars {
		if i != 0 && i%3 == 0 {
			resultChars = append(resultChars, '-')
		}

		if i%3 == 0 && (len(cleanedChars)-i == 2 || len(cleanedChars)-i == 3) {
			resultChars = append(resultChars, cleanedChars[i:]...)
			break
		}

		if i%3 == 0 && len(cleanedChars)-i == 4 {
			resultChars = append(resultChars, cleanedChars[i:i+2]...)
			resultChars = append(resultChars, '-')
			resultChars = append(resultChars, cleanedChars[i+2:]...)
			break
		}
		resultChars = append(resultChars, char)
	}

	return string(resultChars)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	number := strings.Replace(temp, "]", "", -1)
	fmt.Printf("number = %s\n", number)

	timeStart := time.Now()

	result := reformatNumber(number)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
