package main

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func reorderLogFiles(logs []string) []string {
	size := len(logs)

	letters := make([]string, 0, size)
	digits := make([]string, 0, size)

	for _, log := range logs {
		if isDigit(log) {
			digits = append(digits, log)
		} else {
			letters = append(letters, log)
		}
	}

	sort.Slice(letters, func(i int, j int) bool {
		li := letters[i]
		li = li[strings.Index(li, " "):]
		lj := letters[j]
		lj = lj[strings.Index(lj, " "):]
		return strings.Compare(li, lj) <= 0
	})

	return append(letters, digits...)
}

func isDigit(log string) bool {
	b := log[strings.Index(log, " ")+1]
	return '0' <= b && b <= '9'
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	logs := strings.Split(temp, ",")

	fmt.Printf("logs = %s\n", logs)

	timeStart := time.Now()

	result := reorderLogFiles(logs)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
