package solution

import (
	"fmt"
	"strings"
	"time"
)

func numTeams(rating []int) int {
	// 12ms
	arrAsc, arrDesc := make([]int, len(rating)), make([]int, len(rating))
	ans := 0
	for i, _ := range rating {
		for j := 0; j < i; j++ {
			if rating[i] > rating[j] {
				arrAsc[i]++
				ans += arrAsc[j]
			} else if rating[i] < rating[j] {
				arrDesc[i]++
				ans += arrDesc[j]
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	rating := StringToIntArray(flds)
	fmt.Printf("rating = [%s]\n", IntArrayToString(rating))

	timeStart := time.Now()

	result := numTeams(rating)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
