package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func checkInclusion(s1 string, s2 string) bool {
	// 0ms
	if len(s1) > len(s2) {
		return false
	}

	leftptr := 0;
	table1 := make([]int, 26)
	table2 := make([]int, 26)
	size := len(s1);

	for i := 0; i < size; i++ {
		table1[s1[i] - 'a']++;
		table2[s2[i] - 'a']++;
	}
	for i := size; i < len(s2); i++ {
		if check(table1, table2) {
			return true
		}
		table2[s2[leftptr] - 'a']--
		table2[s2[i] - 'a']++
		leftptr++
	}
	if check(table1, table2) {
			return true
	}
	return false
}

func check(table1 []int, table2 []int) bool {
	for i := 0; i < 26; i++ {
		if table1[i] != table2[i] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s1 := flds[0]
	s2 := flds[1]
	fmt.Printf("s1 = %s\n", s1)
	fmt.Printf("s2 = %s\n", s2)

	timeStart := time.Now()

	result := checkInclusion(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
