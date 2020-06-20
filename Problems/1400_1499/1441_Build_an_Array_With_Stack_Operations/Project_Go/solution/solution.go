package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func buildArray(target []int, n int) []string {
	// 0ms
	res := make([]string, 0)
	pos, i := 1, 0

	for i < len(target) {
		if target[i] == pos {
			res = append(res, "Push")
			i++
		} else {
			res = append(res, "Push")
			res = append(res, "Pop")
		}
		pos++
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	target := StringToIntArray(flds[0])
	n, _ := strconv.Atoi(flds[1])

	fmt.Printf("target = [%s], n = %d\n", IntArrayToString(target), n)

	timeStart := time.Now()

	result := buildArray(target, n)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
