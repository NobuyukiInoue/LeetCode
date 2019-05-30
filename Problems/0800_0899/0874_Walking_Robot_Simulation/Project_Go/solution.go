package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func robotSim3(commands []int, obstacles [][]int) int {
	// 3612ms
	directions := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

	x, y, direction, maxDistSquare := 0, 0, 1, 0
	for i, _ := range commands {
		if commands[i] == -2 {
			direction--
			if direction < 0 {
				direction += 4
			}
		} else if commands[i] == -1 {
			direction++
			direction %= 4
		} else {
			step := 0
			Hit := false
			for step < commands[i] {
				for _, val := range obstacles {
					if val[0] == x+directions[direction][0] {
						if val[1] == y+directions[direction][1] {
							Hit = true
							break
						}
					}
				}
				if Hit {
					break
				}

				x += directions[direction][0]
				y += directions[direction][1]
				step++
			}
		}
		maxDistSquare = max(maxDistSquare, x*x+y*y)
	}

	return maxDistSquare
}

func robotSim(commands []int, obstacles [][]int) int {
	// 1716ms
	directions := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

	x, y, direction, maxDistSquare := 0, 0, 1, 0
	for i, _ := range commands {
		if commands[i] == -2 {
			direction--
			if direction < 0 {
				direction += 4
			}
		} else if commands[i] == -1 {
			direction++
			direction %= 4
		} else {
			step := 0
			for step < commands[i] {
				if positionHit(obstacles, x+directions[direction][0], y+directions[direction][1]) {
					break
				}
				x += directions[direction][0]
				y += directions[direction][1]
				step++
			}
		}
		maxDistSquare = max(maxDistSquare, x*x+y*y)
	}

	return maxDistSquare
}

func positionHit(obstacles [][]int, x int, y int) bool {
	for _, val := range obstacles {
		if val[0] == x {
			if val[1] == y {
				return true
			}
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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i, val := range numsStr {
		nums[i], _ = strconv.Atoi(val)
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	str_args := strings.Split(temp, "],[[")

	commands := str2IntArray(strings.Replace(str_args[0], "[[", "", -1))
	fmt.Printf("commands = [%s]\n", printIntArray(commands))

	flds := strings.Split(strings.Replace(str_args[1], "]]]", "", -1), "],[")

	var obstacles [][]int

	if len(flds) > 0 && flds[0] != "" {
		obstacles = make([][]int, len(flds))

		fmt.Printf("obstacles = [")
		for i, val := range flds {
			obstacles[i] = str2IntArray(val)
			if i == 0 {
				fmt.Printf("[%s]", printIntArray(obstacles[i]))
			} else {
				fmt.Printf(",[%s]", printIntArray(obstacles[i]))
			}
		}
		fmt.Printf("]\n")

	} else {
		obstacles = make([][]int, 0)
		fmt.Printf("obstacles = [[]]\n")
	}

	timeStart := time.Now()

	result := robotSim(commands, obstacles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
