package solution

import (
	"fmt"
	"math"
	"strings"
	"time"
)

func maximumDetonation(bombs [][]int) int {
	// 52ms
	if len(bombs) == 0 {
		return 0
	}
	max := 1
	detonationMap := make(map[int][]int)

	for i := 0; i < len(bombs); i++ {
		for j := 0; j < len(bombs); j++ {
			if i != j {
				if float64(bombs[i][2]) >= distance(bombs[i], bombs[j]) {
					if arr, ok := detonationMap[i]; ok {
						arr = append(arr, j)
						detonationMap[i] = arr
					} else {
						var arr []int
						arr = append(arr, j)
						detonationMap[i] = arr
					}
				}
			}
		}
	}

	for key := range detonationMap {
		detonated := []int{key}
		queue := []int{key}
		visited := make(map[int]bool)
		visited[key] = true

		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]

			for _, val := range detonationMap[cur] {
				if !visited[val] {
					detonated = append(detonated, val)
					visited[val] = true
					queue = append(queue, val)
				}
			}
		}
		if len(detonated) == len(bombs) {
			return len(bombs)
		}

		if len(detonated) > max {
			max = len(detonated)
		}
	}
	return max
}

func distance(a []int, b []int) float64 {
	ret := math.Sqrt(math.Pow(float64(a[0]-b[0]), 2) + math.Pow(float64(a[1]-b[1]), 2))
	return ret
}

/*
func maximumDetonation2(bombs [][]int) int {
	// 68ms
	direct := make([][]int, len(bombs))
	for i, v0 := range bombs {
		for j, v1 := range bombs {
			if i == j {
				continue
			}
			if (v0[0]-v1[0])*(v0[0]-v1[0])+(v0[1]-v1[1])*(v0[1]-v1[1]) <= v0[2]*v0[2] {
				direct[i] = append(direct[i], j)
			}
		}
	}
	md := 0
	for i := range bombs {
		linker := make(map[int]struct{})
		dfs(direct, i, make([]bool, len(bombs)), linker)
		if len(linker) > md {
			md = len(linker)
		}
	}
	return md
}

func dfs(direct [][]int, index int, feet []bool, linker map[int]struct{}) {
	if feet[index] {
		return
	}
	feet[index] = true
	linker[index] = struct{}{}
	for _, bomb := range direct[index] {
		dfs(direct, bomb, feet, linker)
	}
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	bombs := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		bombs[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("bombs = %s\n", IntIntArrayToGridString(bombs))

	timeStart := time.Now()

	result := maximumDetonation(bombs)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
