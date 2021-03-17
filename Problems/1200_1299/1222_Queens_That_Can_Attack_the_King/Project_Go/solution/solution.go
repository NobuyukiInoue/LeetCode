package solution

import (
	"fmt"
	"strings"
	"time"
)

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	// 0ms
    result := make([][]int, 0)
	var move = [][]int{{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}}

	for i := 0; i < 8; i++ {
		x := king[0] + move[i][0]
		y := king[1] + move[i][1]
		for isValid(x, y) {
			if queenExist(x, y, queens) {
				result = append(result, []int{x, y})
				break
			}
			x += move[i][0]
			y += move[i][1]
		}
	}

	return result
}

func queenExist(x int, y int, queens [][]int) bool {
	for i := 0; i < len(queens); i++ {
		if queens[i][0] == x && queens[i][1] == y {
			return true
		}
	}
	return false
}

func isValid(x int, y int) bool {
	if  x >= 0 && x < 8 && y >= 0 && y < 8 {
		return true
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "]],[[")

	queensFlds := strings.Split(flds[0], "],[")
	queens := make([][]int, len(queensFlds))
	for i := 0; i < len(queensFlds); i++ {
		queens[i] = StringToIntArray(queensFlds[i])
	}
	fmt.Printf("queens = %s\n", IntIntArrayToString(queens))

	king := StringToIntArray(flds[1])
	fmt.Printf("king = %s\n", IntArrayToString(king))

	timeStart := time.Now()

	result := queensAttacktheKing(queens, king)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n",  IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
