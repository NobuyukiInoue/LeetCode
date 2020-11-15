package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func carFleet(target int, position []int, speed []int) int {
	// 32ms
	if len(position) < 1 || len(speed) < 1 {
		return 0
	}
	posToSpeed := map[int]int{}
	for i := 0; i < len(position); i++ {
		posToSpeed[position[i]] = speed[i]
	}
	sort.Sort(sort.IntSlice(position))
	leaderTime := float32(target-position[len(position)-1]) / float32(posToSpeed[position[len(position)-1]])
	currGroups := 1
	for i := len(position) - 2; i >= 0; i-- {
		currTime := float32(target-position[i]) / float32(posToSpeed[position[i]])
		if currTime > leaderTime {
			currGroups++
			leaderTime = currTime
		}
	}
	return currGroups
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	target, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))
	var position []int
	if len(flds[1]) > 0 {
		position = StringToIntArray(flds[1])
	}

	flds2 := strings.Replace(flds[2], "]]", "", -1)
	var speed []int
	if len(flds2) > 0 {
		speed = StringToIntArray(flds2)
	}
	fmt.Printf("target = %d, position = [%s], speed = [%s]\n", target, IntArrayToString(position), IntArrayToString(speed))

	timeStart := time.Now()

	result := carFleet(target, position, speed)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
