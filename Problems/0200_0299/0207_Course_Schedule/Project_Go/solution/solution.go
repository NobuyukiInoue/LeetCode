package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canFinish(numCourses int, prerequisites [][]int) bool {
	// 8ms
	G := make([][]int, numCourses)
	degree := make([]int, numCourses)
	bfs := make([]int, 0)

	for i := 0; i < numCourses; i++ {
		G[i] = make([]int, 0)
	}

	for _, e := range prerequisites {
		G[e[1]] = append(G[e[1]], e[0])
		degree[e[0]]++
	}

	for i := 0; i < numCourses; i++ {
		if degree[i] == 0 {
			bfs = append(bfs, i)
		}
	}

	for i := 0; i < len(bfs); i++ {
		for _, j := range G[bfs[i]] {
			degree[j]--
			if degree[j] == 0 {
				bfs = append(bfs, j)
			}
		}
	}

	return len(bfs) == numCourses
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArrayToString(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds[0] = strings.Replace(flds[0], "[", "", -1)
	numCourses, _ := strconv.Atoi(flds[0])
	fmt.Printf("numCorses = %d\n", numCourses)

	flds[1] = strings.Replace(flds[1], "]]]", "", -1)
	dataStr := strings.Split(flds[1], "],[")

	var prerequisites [][]int
	if len(dataStr) > 0 {
		prerequisites = make([][]int, len(dataStr))
		fmt.Printf("prerequisites = [\n")
		for i := 0; i < len(prerequisites); i++ {
			prerequisites[i] = strToIntArray(dataStr[i])
			if i == 0 {
				fmt.Printf("  %s\n", intArrayToString(prerequisites[i]))
			} else {
				fmt.Printf(", %s\n", intArrayToString(prerequisites[i]))
			}
		}
		fmt.Printf("]\n")
	} else {
		prerequisites = make([][]int, 0)
	}

	timeStart := time.Now()

	result := canFinish(numCourses, prerequisites)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
