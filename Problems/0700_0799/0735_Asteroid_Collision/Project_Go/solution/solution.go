package solution

import (
	"fmt"
	"strconv"
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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(nums []int) string {
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	asteroids := str2IntArray(flds)
	fmt.Printf("asteroids = [%s]\n", intArrayToString(asteroids))

	timeStart := time.Now()

	result := asteroidCollision(asteroids)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", intArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
