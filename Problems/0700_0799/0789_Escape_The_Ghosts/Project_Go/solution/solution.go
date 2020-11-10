package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func escapeGhosts(ghosts [][]int, target []int) bool {
	// 0ms
	t := myAbs(target[0]) + myAbs(target[1])
	for _, g := range ghosts {
		if t >= myAbs(g[0]-target[0])+myAbs(g[1]-target[1]) {
			return false
		}
	}
	return true
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)

	flds := strings.Split(temp, "]],[")
	flds0 := strings.Split(strings.Replace(flds[0], "[[[", "", -1), "],[")

	ghosts := make([][]int, len(flds0))
	for i := 0; i < len(flds0); i++ {
		ghosts[i] = StringToIntArray(flds0[i])
	}
	target := StringToIntArray(strings.Replace(flds[1], "]]", "", -1))

	fmt.Printf("ghosts = %s, target = [%s]\n", IntIntArrayToString(ghosts), IntArrayToString(target))

	timeStart := time.Now()

	result := escapeGhosts(ghosts, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
