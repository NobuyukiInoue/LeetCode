package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func robotSim(commands []int, obstacles [][]int) int {
	// 88ms
	directions := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

	max := 30000
	obs := make([][]int, max-(-max)+1)

	for i, _ := range obs {
		obs[i] = make([]int, 0)
	}

	for i, _ := range obstacles {
		obs[obstacles[i][0]+max+1] = append(obs[obstacles[i][0]+max+1], obstacles[i][1])
	}

	/*
		for _, t_obs := range obs {
			sort.Slice(t_obs, func(i, j int) bool {
				return t_obs[i] < t_obs[j]
			})
		}
	*/

	x, y, direction, maxDistSquare := 0, 0, 1, 0
	for _, cmd := range commands {
		if cmd == -2 {
			direction--
			if direction < 0 {
				direction += 4
			}
		} else if cmd == -1 {
			direction++
			direction %= 4
		} else {
			for step := 0; step < cmd; step++ {
				nextX := x + directions[direction][0]
				nextY := y + directions[direction][1]
				if positionHit2(&obs[nextX+max+1], nextY) {
					break
				}
				x, y = nextX, nextY
			}
		}
		maxDistSquare = max2(maxDistSquare, x*x+y*y)
	}
	return maxDistSquare
}

func positionHit2(obs *[]int, y int) bool {
	for _, val := range *obs {
		if val == y {
			return true
		}
	}
	return false
}

/*
func positionHit2(obs *[]int, y int) bool {
	for _, val := range *obs {
		if val < y {
			continue
		} else if val == y {
			return true
		} else {
			return false
		}
	}
	return false
}
*/

func max2(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func robotSim_old(commands []int, obstacles [][]int) int {
	// 1108ms
	directions := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

	// sort obstacles
	sort.Slice(obstacles, func(i, j int) bool {
		return obstacles[i][0] < obstacles[j][0]
	})

	x, y, direction, maxDistSquare := 0, 0, 1, 0
	for _, cmd := range commands {
		if cmd == -2 {
			direction--
			if direction < 0 {
				direction += 4
			}
		} else if cmd == -1 {
			direction++
			direction %= 4
		} else {
			for step := 0; step < cmd; step++ {
				nextX := x + directions[direction][0]
				nextY := y + directions[direction][1]
				if positionHit(&obstacles, nextX, nextY) {
					break
				}
				x, y = nextX, nextY
			}
		}
		maxDistSquare = max(maxDistSquare, x*x+y*y)
	}

	return maxDistSquare
}

func positionHit(obstacles *[][]int, x int, y int) bool {
	for _, val := range *obstacles {
		if val[0] < x {
			continue
		} else if val[0] == x && val[1] == y {
			return true
		} else if val[0] > x {
			return false
		}
	}
	return false
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	str_args := strings.Split(temp, "],[[")

	commands := StringToIntArray(strings.Replace(str_args[0], "[[", "", -1))
	fmt.Printf("commands = [%s]\n", IntArrayToString(commands))

	flds := strings.Split(strings.Replace(str_args[1], "]]]", "", -1), "],[")

	var obstacles [][]int

	if len(flds) > 0 && flds[0] != "" {
		obstacles = make([][]int, len(flds))

		for i, val := range flds {
			obstacles[i] = StringToIntArray(val)
		}
		fmt.Printf("]\n")

	} else {
		obstacles = make([][]int, 0)
	}

	fmt.Printf("obstacles = %s\n", IntIntArrayToString(obstacles))

	timeStart := time.Now()

	result := robotSim(commands, obstacles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
