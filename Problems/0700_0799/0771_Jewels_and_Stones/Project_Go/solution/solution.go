package solution

import (
	"fmt"
	"strings"
	"time"
)

func numJewelsInStones(J string, S string) int {
	dic := make(map[string]int)
	runeJ := []rune(J)
	runeS := []rune(S)

	for i, _ := range runeJ {
		dic[string(runeJ[i])]++
	}

	result := 0
	for i, _ := range runeS {
		if dic[string(runeS[i])] > 0 {
			result++
		}
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	words := strings.Split(temp, "],[")
	J := words[0]
	S := words[1]

	fmt.Printf("J = %s, S = %s\n", J, S)

	timeStart := time.Now()

	result := numJewelsInStones(J, S)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
