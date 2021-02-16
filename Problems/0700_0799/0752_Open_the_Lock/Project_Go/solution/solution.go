package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func openLock(deadends []string, target string) int {
	// 12ms
	dead := make([]bool, 10000)

	for _, d := range deadends {
		temp, _ := strconv.Atoi(d)
		dead[temp] = true
	}

	if dead[0] {
		return -1
	}

	dead[0] = true

	t, _ := strconv.Atoi(target)
	ans := 0

	list := make([]int, 0)
	list = append(list, 0)

	for len(list) > 0 {
		n := len(list)
		for i := 0; i < n; i++ {
			var cur int
			if n > 0 {
				cur = list[0]
				if n == 1 {
					list = make([]int, 0)
				} else {
					list = list[1:]
				}
			} else {
				cur = 0
			}
			if cur == t {
				return ans
			}
			for m := 1; m <= 1000; m *= 10 {
				var x, y int

				x = (cur % (m * 10)) / m
				if x == 9 {
					y = cur - (m * 9)
				} else {
					y = cur + m
				}

				if !dead[y] {
					list = append(list, y)
					dead[y] = true
				}
				if x == 0 {
					y = cur + (m * 9)
				} else {
					y = cur - m
				}
				if !dead[y] {
					list = append(list, y)
					dead[y] = true
				}
			}
		}
		ans++
	}
	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	deadends := strings.Split(flds[0], ",")
	target := flds[1]
	fmt.Printf("deadends  = %s\n", deadends)
	fmt.Printf("target = %s\n", target)

	timeStart := time.Now()

	result := openLock(deadends, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
