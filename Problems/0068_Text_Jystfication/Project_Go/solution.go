package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func fullJustify(words []string, maxWidth int) []string {
	var result []string
	end := 0
	for end < len(words) {
		sum := 0
		start := end
		for end < len(words) && sum+len(words[end]) <= maxWidth {
			sum += len(words[end]) + 1
			end++
		}

		newString := ""
		if end >= len(words) {
			for i := start; i < end-1; i++ {
				newString += words[i] + " "
			}

			newString += words[end-1]
			count := maxWidth - len(newString)
			for j := 0; j < count; j++ {
				newString += " "
			}

			result = append(result, newString)
			continue
		}

		spaces := maxWidth - sum
		spaces += end - start
		noOfGaps := end - start - 1

		if noOfGaps == 0 {
			newString += words[end-1]

			for j := 0; j < maxWidth-len(words[end-1]); j++ {
				newString += " "
			}
			result = append(result, newString)
			continue
		}

		spaceBetweenWords := spaces / noOfGaps
		extraSpaces := spaces % noOfGaps

		for i := start; i < end-1; i++ {
			newString += words[i]
			for j := 0; j < spaceBetweenWords; j++ {
				newString += " "
			}
			if extraSpaces > 0 {
				newString += " "
				extraSpaces--
			}
		}
		newString += words[end-1]
		result = append(result, newString)
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	words := strings.Split(flds[0], ",")
	maxWidth, _ := strconv.Atoi(flds[1])

	fmt.Printf("nums = %s, maxWidth = %d\n", words, maxWidth)

	timeStart := time.Now()

	result := fullJustify(words, maxWidth)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
