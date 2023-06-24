package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func executeInstructions(n int, startPos []int, s string) []int {
	// 12ms - 17ms
	s_len := len(s)
	ans := make([]int, s_len)
	for i := 0; i < s_len; i++ {
		ans[i] = helper(n, startPos[1], startPos[0], s[i:])
	}
	return ans
}

func helper(n int, x int, y int, s string) int {
	cnt := 0
	for _, inst := range s {
		if inst == 'L' {
			x--
		} else if inst == 'R' {
			x++
		} else if inst == 'U' {
			y--
		} else if inst == 'D' {
			y++
		}
		if x < 0 || y < 0 || x == n || y == n {
			break
		}
		cnt++
	}
	return cnt
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	startPos := StringToIntArray(flds[1])
	s := flds[2]
	fmt.Printf("n = %d, startPos = [%s], s = %s\n", n, IntArrayToString(startPos), s)

	timeStart := time.Now()

	result := executeInstructions(n, startPos, s)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
