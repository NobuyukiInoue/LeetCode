package solution

import (
	"fmt"
	"strings"
	"time"
)

func isWinner(player1 []int, player2 []int) int {
	// 25ms - 31ms
	score1 := getScore(player1)
	score2 := getScore(player2)
	if score1 > score2 {
		return 1
	} else if score1 < score2 {
		return 2
	}
	return 0
}

func getScore(nums []int) int {
	score, cnt := 0, 0
	for _, num := range nums {
		if cnt > 0 {
			score += num * 2
			cnt--
		} else {
			score += num
		}
		if num == 10 {
			cnt = 2
		}
	}
	return score
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	player1 := StringToIntArray(flds[0])
	player2 := StringToIntArray(flds[1])
	fmt.Printf("player1 = [%s], player2 = [%s]\n", IntArrayToString(player1), IntArrayToString(player2))

	timeStart := time.Now()

	result := isWinner(player1, player2)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
