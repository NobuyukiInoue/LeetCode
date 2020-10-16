package solution

import (
	"bytes"
	"fmt"
	"strings"
	"time"
)

func reorderSpaces(text string) string {
	// 0ms
	var spaceCount int
	for _, ch := range text {
		if ch == ' ' {
			spaceCount++
		}
	}

	words := strings.Fields(text)
	var spacesBetween, spacesAfter int
	if len(words) <= 1 {
		spacesAfter = spaceCount
	} else {
		spacesBetween = spaceCount / (len(words) - 1)
		spacesAfter = spaceCount % (len(words) - 1)
	}

	var buf bytes.Buffer
	for i, w := range words {
		buf.WriteString(w)
		if i == len(words)-1 {
			break
		}
		for j := 0; j < spacesBetween; j++ {
			buf.WriteString(" ")
		}
	}

	for i := 0; i < spacesAfter; i++ {
		buf.WriteString(" ")
	}
	return buf.String()
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	text := strings.Replace(temp, "]", "", -1)
	fmt.Printf("text = %s\n", text)

	timeStart := time.Now()

	result := reorderSpaces(text)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
