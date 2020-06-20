package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func lastStoneWeight(stones []int) int {
	for len(stones) > 1 {
		sort.Ints(stones)
		diff := stones[len(stones)-1] - stones[len(stones)-2]
		stones = stones[:len(stones)-2]
		stones = append(stones, diff)
	}
	return stones[0]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	stones := StringToIntArray(flds)
	fmt.Printf("stones = [%s]\n", IntArrayToString(stones))

	timeStart := time.Now()

	result := lastStoneWeight(stones)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
