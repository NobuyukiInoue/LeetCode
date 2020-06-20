package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func distributeCandies(candies []int) int {
	kinds := make([]int, 0, len(candies))
	encountered := map[int]bool{}
	for i := 0; i < len(candies); i++ {
		if !encountered[candies[i]] {
			encountered[candies[i]] = true
			kinds = append(kinds, candies[i])
		}
	}

	if len(kinds) >= len(candies)/2 {
		return len(candies) / 2
	} else {
		return len(kinds)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	candies := make([]int, len(flds))
	for i, _ := range flds {
		candies[i], _ = strconv.Atoi(flds[i])
	}

	fmt.Printf("candies = %s\n", IntArrayToString(candies))

	timeStart := time.Now()

	result := distributeCandies(candies)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
