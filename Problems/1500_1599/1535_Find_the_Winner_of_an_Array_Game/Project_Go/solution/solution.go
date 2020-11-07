package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getWinner(arr []int, k int) int {
	// 100ms
	cur := arr[0]
	win := 0
	for i := 1; i < len(arr); i++ {
		if arr[i] > cur {
			cur = arr[i]
			win = 0
		}
		win++
		if win == k {
			break
		}
	}
	return cur
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("arr = [%s], k = %d\n", IntArrayToString(arr), k)

	timeStart := time.Now()

	result := getWinner(arr, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
