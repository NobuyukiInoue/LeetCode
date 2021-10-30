package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minMovesToSeat(seats []int, students []int) int {
	// 8ms
	sort.Sort(sort.IntSlice(seats))
	sort.Sort(sort.IntSlice(students))
	ans := 0
	for i := 0; i < len(seats); i++ {
		ans += myAbs(seats[i] - students[i])
	}
	return ans
}

func myAbs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	seats := StringToIntArray(flds[0])
	students := StringToIntArray(flds[1])
	fmt.Printf("seats = [%s], students = [%s]\n", IntArrayToString(seats), IntArrayToString(students))

	timeStart := time.Now()

	result := minMovesToSeat(seats, students)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
