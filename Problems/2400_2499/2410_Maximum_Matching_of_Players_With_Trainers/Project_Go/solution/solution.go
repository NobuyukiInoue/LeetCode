package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func matchPlayersAndTrainers(players []int, trainers []int) int {
	// 167ms - 170ms
	sort.Sort(sort.IntSlice(players))
	sort.Sort(sort.IntSlice(trainers))
	res, i, j := 0, 0, 0
	for i < len(players) && j < len(trainers) {
		if players[i] <= trainers[j] {
			res++
			i++
		}
		j++
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	players := StringToIntArray(flds[0])
	trainers := StringToIntArray(flds[1])

	fmt.Printf("players = [%s], trainers = [%s]\n", IntArrayToString(players), IntArrayToString(trainers))

	timeStart := time.Now()

	result := matchPlayersAndTrainers(players, trainers)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
