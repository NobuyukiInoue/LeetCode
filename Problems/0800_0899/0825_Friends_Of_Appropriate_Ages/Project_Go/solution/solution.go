package solution

import (
	"fmt"
	"strings"
	"time"
)

func numFriendRequests(ages []int) int {
	// 40ms
	m := make(map[int]int)
	for age := 1; age <= 120; age++ {
		m[age] = 0
	}
	for _, age := range ages {
		m[age] += 1
	}

	res := 0
	for age := 1; age <= 120; age++ {
		count, _ := m[age]
		if count == 0 {
			continue
		}

		// friends with the same age
		if float32(age) > 0.5*float32(age)+7 {
			res += count * (count - 1)
		}

		// friends with different ages
		for age2 := 1; age2 < age; age2++ {
			count2, _ := m[age2]
			if count2 == 0 {
				continue
			}
			if 0.5*float32(age)+7 >= float32(age2) {
				continue
			}
			res += count * count2
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	ages := StringToIntArray(flds)
	fmt.Printf("ages = [%s]\n", IntArrayToString(ages))

	timeStart := time.Now()

	result := numFriendRequests(ages)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
