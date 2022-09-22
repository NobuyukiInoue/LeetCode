package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkDistances(s string, distance []int) bool {
	// 10ms - 11ms
	for i := 0; i < 26; i++ {
		ch := string('a' + i)
		p1 := strings.Index(s, ch)
		if p1 == -1 {
			continue
		}
		p2 := strings.LastIndex(s, ch)
		if p2 == -1 {
			continue
		}
		if p2-p1 != distance[i]+1 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	distance := StringToIntArray(flds[1])

	fmt.Printf("s = \"%s\", distance = [%s]\n", s, IntArrayToString(distance))

	timeStart := time.Now()

	result := checkDistances(s, distance)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
