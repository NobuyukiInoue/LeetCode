package solution

import (
	"fmt"
	"strings"
	"time"
)

// 92ms

func totalFruit(tree []int) int {
	var fruits []int = []int { -1, -1 }
	var count []int = []int {0, 0}

	last_count, last, total := 0, 1, 0

	for _, t := range(tree) {
		if indexOf(fruits, t) >= 0 {
			if t != fruits[last] {
				last = notlast(last)
				last_count = count[last]
			}
			count[last]++
		} else {
			total = myMax(total, arraySum(count))
			count[last] -= last_count
			last = notlast(last)
			fruits[last] = t
			count[last] = 1
			last_count = 0
		}
	}

	total = myMax(total, arraySum(count))
	return total
}

func notlast(last int) int{
	if last == 1 {
		return 0
	}
	return 1
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func indexOf(data []int, target int) int {
	for i := 0; i < len(data); i++ {
		if target == data[i] {
			return i
		}
	}
	return -1
}
func arraySum(data []int) int {
	if data == nil {
		return 0
	}
	if len(data) <= 0 {
		return 0
	}

	total := data[0]
	for i := 1; i < len(data); i++ {
		total += data[i]
	}

	return total
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	tree := StringToIntArray(flds)
	fmt.Printf("tree = [%s]\n", IntArrayToString(tree))

	timeStart := time.Now()

	result := totalFruit(tree)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
