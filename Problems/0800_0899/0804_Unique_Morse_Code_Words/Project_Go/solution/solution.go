package solution

import (
	"fmt"
	"strings"
	"time"
)

func uniqueMorseRepresentations(words []string) int {
	dic := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
		".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
		"...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}

	resultCodes := words

	for i := 0; i < len(words); i++ {
		currentMorseCode := ""
		for j := 0; j < len(words[i]); j++ {
			currentMorseCode += dic[words[i][j]-"a"[0]]
		}
		resultCodes[i] = currentMorseCode
	}

	/*
		for i, curr := range resultCodes {
			fmt.Printf("resultCodes[%d] = %s\n", i, curr)
		}
	*/

	m := make(map[string]bool)
	uniq := []string{}
	for _, ele := range resultCodes {
		if !m[ele] {
			m[ele] = true
			uniq = append(uniq, ele)
		}
	}

	return (len(uniq))
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)

	words := strings.Split(temp, ",")

	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := uniqueMorseRepresentations(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
