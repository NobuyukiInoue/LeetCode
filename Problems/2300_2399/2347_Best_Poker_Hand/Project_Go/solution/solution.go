package solution

import (
	"fmt"
	"strings"
	"time"
)

func bestHand(ranks []int, suits []byte) string {
	// 0ms
	var cnt [14]int
	cnt_max := 0
	for _, card := range ranks {
		cnt[card]++
		cnt_max = myMax(cnt_max, cnt[card])
	}
	if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4] {
		return "Flush"
	} else if cnt_max >= 3 {
		return "Three of a Kind"
	} else if cnt_max == 2 {
		return "Pair"
	} else {
		return "High Card"
	}
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	ranks := StringToIntArray(flds[0])
	suits := []byte(strings.Replace(flds[1], ",", "", -1))
	fmt.Printf("ranks = [%s], suits = \"%s\"\n", IntArrayToString(ranks), suits)

	timeStart := time.Now()

	result := bestHand(ranks, suits)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
