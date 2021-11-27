package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func memLeak(memory1 int, memory2 int) []int {
	// 7ms
	var i int
	for i = 0; true; i++ {
		if memory1 >= memory2 {
			if memory1 < i {
				break
			}
			memory1 -= i
		} else {
			if memory2 < i {
				break
			}
			memory2 -= i
		}
	}
	return []int{i, memory1, memory2}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	memory1, _ := strconv.Atoi(flds[0])
	memory2, _ := strconv.Atoi(flds[1])
	fmt.Printf("memory1 = %d, memory2 = %d\n", memory1, memory2)

	timeStart := time.Now()

	result := memLeak(memory1, memory2)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
