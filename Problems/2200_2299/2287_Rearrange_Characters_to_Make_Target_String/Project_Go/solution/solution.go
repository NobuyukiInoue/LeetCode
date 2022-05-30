package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func rearrangeCharacters(s string, target string) int {
	// 3ms
	var cnt1 [26]int
	var cnt2 [26]int
	for _, ch := range s {
		cnt1[ch-'a']++
	}
	for _, ch := range target {
		cnt2[ch-'a']++
	}
	res := math.MaxInt32
	for i := 0; i < len(cnt1); i++ {
		if cnt2[i] != 0 {
			res = myMin(res, cnt1[i]/cnt2[i])
		}
	}
	return res
}

func myMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	s, target := flds[0], flds[1]
	fmt.Printf("s = %s, target = %s\n", s, target)

	timeStart := time.Now()

	result := rearrangeCharacters(s, target)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
