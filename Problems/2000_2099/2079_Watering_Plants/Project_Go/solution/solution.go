package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func wateringPlants(plants []int, capacity int) int {
	// 3ms
	ans, water := 0, capacity
	for i, cur := range plants {
		if cur <= water {
			water -= cur
			ans++
		} else {
			water = capacity - cur
			ans += 2*i + 1
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	plants := StringToIntArray(flds[0])
	capacity, _ := strconv.Atoi(flds[1])
	fmt.Printf("plants = [%s], capacity = %d\n", IntArrayToString(plants), capacity)

	timeStart := time.Now()

	result := wateringPlants(plants, capacity)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
