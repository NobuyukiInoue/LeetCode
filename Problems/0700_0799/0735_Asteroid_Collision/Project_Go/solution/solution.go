package solution

import (
	"fmt"
	"strings"
	"time"
)

func asteroidCollision(asteroids []int) []int {
	// 8ms
	stack := make([]int, 0)
	for _, asteroid := range asteroids {
		if asteroid < 0 {
			for asteroid < 0 && len(stack) > 0 && stack[len(stack)-1] > 0 {
				if stack[len(stack)-1] > myAbs(asteroid) {
					asteroid = 0
				} else if stack[len(stack)-1] == myAbs(asteroid) {
					stack = stack[:len(stack)-1]
					asteroid = 0
				} else {
					stack = stack[:len(stack)-1]
				}
			}
			if asteroid != 0 {
				stack = append(stack, asteroid)
			}
		} else {
			stack = append(stack, asteroid)
		}
	}
	return stack
}

func myAbs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	asteroids := StringToIntArray(flds)
	fmt.Printf("asteroids = [%s]\n", IntArrayToString(asteroids))

	timeStart := time.Now()

	result := asteroidCollision(asteroids)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
