package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func numRescueBoats(people []int, limit int) int {
	// 74ms - 76ms
	sort.Sort(sort.IntSlice(people))
	ans, i, j := 0, 0, len(people)-1
	for i <= j {
		ans++
		if people[i]+people[j] <= limit {
			i++
		}
		j--
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

	people := StringToIntArray(flds[0])
	limit, _ := strconv.Atoi(flds[1])
	fmt.Printf("people = %s, limit = %d\n", IntArrayToString(people), limit)

	timeStart := time.Now()

	result := numRescueBoats(people, limit)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
