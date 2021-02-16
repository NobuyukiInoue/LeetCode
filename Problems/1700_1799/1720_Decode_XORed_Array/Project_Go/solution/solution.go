package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func decode(encoded []int, first int) []int {
	// 28ms
	res := make([]int, len(encoded) + 1)
	res[0] = first
	for i, v := range(encoded) {
		res[i + 1] = v^res[i]
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	encoded := StringToIntArray(flds[0])
	first, _ := strconv.Atoi(flds[1])
	fmt.Printf("encoded = [%s], first = %d\n", IntArrayToString(encoded), first)

	timeStart := time.Now()

	result := decode(encoded, first)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
