package solution

import (
	"fmt"
	"strings"
	"time"
)

func numTilePossibilities(tiles string) int {
	// 0ms
	arr := make([]int, 26)
	for _, v := range tiles {
		arr[v-'A']++
	}
	return helper(arr)
}

func helper(arr []int) int {
	sum := 0
	for i := 0; i < 26; i++ {
		if arr[i] == 0 {
			continue
		}
		sum++
		arr[i]--
		sum += helper(arr)
		arr[i]++
	}
	return sum
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	tiles := strings.Replace(temp, "]", "", -1)
	fmt.Printf("tiles = %s\n", tiles)

	timeStart := time.Now()

	result := numTilePossibilities(tiles)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
