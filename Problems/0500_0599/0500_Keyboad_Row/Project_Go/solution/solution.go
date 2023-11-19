package solution

import (
	"fmt"
	"strings"
	"time"
)

func findWords(words []string) []string {
	// 1ms
	var rowMap [26]int
	rows := []string{"qwertyuiop", "asdfghjkl", "zxcvbnm"}
	for i, row := range rows {
		for _, ch := range row {
			rowMap[ch-'a'] = i
		}
	}
	var res []string
	for _, word := range words {
		row := rowMap[strings.ToLower(word)[0]-'a']
		onSameRow := true
		for _, ch := range strings.ToLower(word) {
			if rowMap[ch-'a'] != row {
				onSameRow = false
				break
			}
		}
		if onSameRow {
			res = append(res, word)
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")

	fmt.Printf("words = [%s]\n", StringArrayToString(words))

	timeStart := time.Now()

	result := findWords(words)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
