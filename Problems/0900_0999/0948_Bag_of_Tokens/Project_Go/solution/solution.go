package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func bagOfTokensScore(tokens []int, P int) int {
	// 4ms
	sort.Ints(sort.IntSlice(tokens))
	res, points, i, j := 0, 0, 0, len(tokens)-1
	for i <= j {
		if P >= tokens[i] {
			P -= tokens[i]
			i++
			points++
			res = myMax(res, points)
		} else if points > 0 {
			points--
			P += tokens[j]
			j--
		} else {
			break
		}
	}
	return res
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	tokens := StringToIntArray(flds[0])
	P, _ := strconv.Atoi(flds[1])
	fmt.Printf("tokens = [%s], P = %d\n", IntArrayToString(tokens), P)

	timeStart := time.Now()

	result := bagOfTokensScore(tokens, P)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
