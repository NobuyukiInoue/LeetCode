package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func allCellsDistOrder(R int, C int, r0 int, c0 int) [][]int {
	counter := make([]int, R+C+1)
	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			dist := abs(r-r0) + abs(c-c0)
			counter[dist+1]++
		}
	}

	for i := 1; i < len(counter); i++ {
		counter[i] += counter[i-1]
	}

	ans := make([][]int, R*C)
	for i := 0; i < len(ans); i++ {
		ans[i] = make([]int, 2)
	}

	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			dist := abs(r-r0) + abs(c-c0)
			ans[counter[dist]] = []int{r, c}
			counter[dist]++
		}
	}

	return ans
}

func abs(x int) int {
	if x >= 0 {
		return x
	} else {
		return -x
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	R, _ := strconv.Atoi(flds[0])
	C, _ := strconv.Atoi(flds[1])
	r0, _ := strconv.Atoi(flds[2])
	c0, _ := strconv.Atoi(flds[3])
	fmt.Printf("R = %d, C = %d, r0 = %d, c0 = %d\n", R, C, r0, c0)

	timeStart := time.Now()

	result := allCellsDistOrder(R, C, r0, c0)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
