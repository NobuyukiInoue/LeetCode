package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findJudge(N int, trust [][]int) int {
	l := make([]int, N+1)
	for i, _ := range trust {
		l[trust[i][1]]++
		l[trust[i][0]]--
	}
	for i := 1; i < N+1; i++ {
		if l[i] == N-1 {
			return i
		}
	}

	return -1
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	N, _ := strconv.Atoi(flds0)
	fmt.Printf("N = %d\n", N)

	flds1 := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	trust := make([][]int, len(flds1))
	for i := 0; i < len(flds1); i++ {
		trust[i] = StringToIntArray(flds1[i])
	}
	fmt.Printf("trust = %s\n", IntIntArrayToString(trust))

	timeStart := time.Now()

	result := findJudge(N, trust)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
