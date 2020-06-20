package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxDistToClosest(seats []int) int {
	n, res := len(seats), 0

	i := 0
	for j := 0; j < n; j++ {
		if seats[j] == 1 {
			if i == 0 {
				res = j
			} else {
				res = max(res, (j-i+1)/2)
			}
			i = j + 1
		}
	}

	res = max(res, n-i)
	return res
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
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	seats := StringToIntArray(flds)
	fmt.Printf("seats = [%s]\n", IntArrayToString(seats))

	timeStart := time.Now()

	result := maxDistToClosest(seats)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
