package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findOrder(numCourses int, prerequisites [][]int) []int {
	// 8ms
	var res []int
	graph := make([][]int, numCourses)
	for _, pre := range prerequisites {
		graph[pre[1]] = append(graph[pre[1]], pre[0])
	}	
	visited := make([]int, numCourses)
	for i := 0; i < numCourses; i ++{
		if visited[i] == 0 && !DFS(i, &visited, &graph, &res) {
			return []int{}
		}
	}
	return reverse(res)
}

func reverse(lists []int) []int {
	var ans []int
	for i := len(lists) - 1; i >= 0; i -- {
		ans = append(ans, lists[i])
	}
	return ans
}

func DFS(curr int, visited *[]int, graph *[][]int, res *[]int) bool{
	if (*visited)[curr] == 1 {
		return true
	}
	if (*visited)[curr] == 2 {
		return false
	}
	(*visited)[curr] = 2
	for _, n := range (*graph)[curr] {
		if !DFS(n, visited, graph, res) {
			return false
		}
	}
	(*visited)[curr] = 1
	*res = append(*res, curr)
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)

	var flds []string

	if strings.Contains(temp, "],[[") {
		flds = strings.Split(temp, "],[[")
	} else {
		flds = strings.Split(temp, "],[")
	}

	flds[0] = strings.Replace(flds[0], "[", "", -1)
	numCourses, _ := strconv.Atoi(flds[0])
	fmt.Printf("numCorses = %d\n", numCourses)

	var prerequisites [][]int

	if strings.Contains(flds[1], "]]]") {
		flds[1] = strings.Replace(flds[1], "]]]", "", -1)
		dataStr := strings.Split(flds[1], "],[")

		if len(dataStr) > 0 {
			prerequisites = make([][]int, len(dataStr))
			for i := 0; i < len(prerequisites); i++ {
				prerequisites[i] = StringToIntArray(dataStr[i])
			}
		} else {
			prerequisites = make([][]int, 0)
		}
	} else {
		prerequisites = make([][]int, 0)
	}

	fmt.Printf("prerequisites = %s\n", IntIntArrayToString(prerequisites))

	timeStart := time.Now()

	result := findOrder(numCourses, prerequisites)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
