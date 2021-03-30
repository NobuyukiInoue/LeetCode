package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func areAlmostEqual(s1 string, s2 string) bool {
	// 0ms
	pos := make([]int , 0)
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			pos = append(pos, i)
		}
		if len(pos) > 2 {
			return false
		}
	}
	return len(pos) == 0 || len(pos) == 2 && s1[pos[0]] == s2[pos[1]] && s1[pos[1]] == s2[pos[0]]
}


func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s1, s2 := flds[0], flds[1]
	fmt.Printf("s1 = %s, s2 = %s\n", s1, s2)

	timeStart := time.Now()

	result := areAlmostEqual(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
