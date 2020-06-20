package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func combinationSum(candidates []int, target int) [][]int {
	// 0ms
	result := make([][]int, 0)

	sort.Ints(candidates)
	dfs(candidates, target, []int{}, &result)

	return result
}

func dfs(candidates []int, target int, current []int, result *[][]int) {
	for i, v := range candidates {
		if target-v <= 0 {
			if target-v == 0 {
				match := make([]int, len(current)+1)
				copy(match, current)
				match[len(current)] = v
				*result = append(*result, match)
			}
			break
		}

		dfs(candidates[i:], target-v, append(current, v), result)
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	candidates := StringToIntArray(flds[0])
	target, _ := strconv.Atoi(flds[1])

	fmt.Printf("candidates = [%s], target = %d\n", IntArrayToString(candidates), target)

	timeStart := time.Now()

	result := combinationSum(candidates, target)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
