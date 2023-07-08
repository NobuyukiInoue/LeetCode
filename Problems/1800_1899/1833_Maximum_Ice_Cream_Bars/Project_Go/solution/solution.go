package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func maxIceCream(costs []int, coins int) int {
	// 188ms - 200ms
	sort.Sort(sort.IntSlice(costs))
	ans := 0
	for _, cost := range costs {
		if coins < cost {
			break
		}
		ans++
		coins -= cost
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	costs := StringToIntArray(flds[0])
	coins, _ := strconv.Atoi(flds[1])
	fmt.Printf("costs = [%s], coins = %d\n", IntArrayToString(costs), coins)

	timeStart := time.Now()

	result := maxIceCream(costs, coins)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
