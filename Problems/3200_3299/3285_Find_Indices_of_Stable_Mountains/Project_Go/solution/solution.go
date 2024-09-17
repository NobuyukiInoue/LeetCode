package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func stableMountains(height []int, threshold int) []int {
	// 0ms
	var ans []int
	for i := 1; i < len(height); i++ {
		if height[i-1] > threshold {
			ans = append(ans, i)
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	height := StringToIntArray(flds[0])
	threshold, _ := strconv.Atoi(flds[1])
	fmt.Printf("height = %s, threshold = %d\n", IntArrayToString(height), threshold)

	timeStart := time.Now()

	result := stableMountains(height, threshold)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
