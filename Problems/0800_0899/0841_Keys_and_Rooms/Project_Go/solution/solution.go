package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

// 4ms
var visited map[int]bool

func canVisitAllRooms(rooms [][]int) bool {
	visited = map[int]bool{}
	dfs(rooms, 0)
	return len(visited) == len(rooms)
}

func dfs(rooms [][]int, room int) {
	if visited[room] == false {
		visited[room] = true
		if rooms[room] != nil {
			for _, key := range rooms[room] {
				dfs(rooms, key)
			}
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	rooms := make([][]int, len(flds))
	for i := 0; i < len(rooms); i++ {
		rooms[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("rooms = %s\n", IntIntArrayToString(rooms))

	timeStart := time.Now()

	result := canVisitAllRooms(rooms)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
