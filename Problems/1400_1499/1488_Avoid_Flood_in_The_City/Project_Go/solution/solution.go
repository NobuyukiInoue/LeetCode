package solution

import (
	"fmt"
	"strings"
	"time"
)

func avoidFlood(rains []int) []int {
	// 372ms
	var zeros []int
	res := make([]int, len(rains))
	m := make(map[int]int)

	for i, r := range rains {
		if r == 0 {
			zeros = append(zeros, i)
			continue
		}

		if _, ok := m[r]; ok {
			zi := -1

			for ti, tzi := range zeros {
				if tzi > m[r] {
					zi = tzi
					zeros = append(zeros[:ti], zeros[ti+1:] ...)
					break
				}
			}

			if zi == -1 {
				return []int{}
			}

			res[zi] = r
		} 
		
		m[r] = i
		res[i] = -1
	}

	for i := range res {
		if res[i] == 0 {
			res[i] = 1
		}
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := avoidFlood(arr)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
