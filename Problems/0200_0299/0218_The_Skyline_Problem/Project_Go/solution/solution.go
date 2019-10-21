package solution

import (
	"container/heap"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func getSkyline(buildings [][]int) [][]int {
	// 36ms
	points := make([]*RoofPoint, len(buildings)*2)
	rightToLeftMap := make(map[*RoofPoint]*RoofPoint)

	for i := 0; i < len(buildings); i++ {
		points[i*2] = &RoofPoint{IsLeft: true, X: buildings[i][0], Height: buildings[i][2]}
		points[1+i*2] = &RoofPoint{IsLeft: false, X: buildings[i][1], Height: buildings[i][2]}
		rightToLeftMap[points[1+i*2]] = points[i*2]
	}
	sort.Sort(ByXAsc(points))

	pq := make(PQ, 0)
	heap.Init(&pq)

	var result [][]int
	for i := 0; i < len(points); i++ {
		point := points[i]
		if point.IsLeft {
			heap.Push(&pq, point)
			if len(result) == 0 {
				result = append(result, []int{point.X, point.Height})
				continue
			}

			highest := pq[0]
			if result[len(result)-1][1] >= highest.Height {
				continue
			}

			if result[len(result)-1][0] == point.X {
				result[len(result)-1][1] = highest.Height

				if len(result) > 1 && result[len(result)-2][1] == highest.Height {
					result = result[:len(result)-1]
				}
			} else {
				result = append(result, []int{point.X, highest.Height})
			}
			continue
		}

		heap.Remove(&pq, rightToLeftMap[point].HeapIdx)

		if len(pq) == 0 {
			if result[len(result)-1][0] < point.X {
				result = append(result, []int{point.X, 0})
			} else {
				result[len(result)-1][1] = 0
			}
			continue
		}

		highest := pq[0]
		if result[len(result)-1][1] > highest.Height {
			if result[len(result)-1][0] < point.X {
				result = append(result, []int{point.X, highest.Height})
			} else {
				result[len(result)-1][1] = highest.Height
			}
		}
	}
	return result
}

type RoofPoint struct {
	HeapIdx int
	IsLeft  bool
	X       int
	Height  int
}

type ByXAsc []*RoofPoint

func (points ByXAsc) Len() int {
	return len(points)
}

func (points ByXAsc) Swap(i, j int) {
	points[i], points[j] = points[j], points[i]
}

func (points ByXAsc) Less(i, j int) bool {
	return points[i].X < points[j].X
}

type PQ []*RoofPoint

func (points PQ) Len() int {
	return len(points)
}

func (points PQ) Swap(i, j int) {
	points[i], points[j] = points[j], points[i]
	points[i].HeapIdx = i
	points[j].HeapIdx = j
}

func (points PQ) Less(i, j int) bool {
	if points[i].Height == points[j].Height {
		return !points[i].IsLeft
	}
	return points[i].Height > points[j].Height
}

func (points *PQ) Push(item interface{}) {
	newP := item.(*RoofPoint)
	newP.HeapIdx = len(*points)
	*points = append(*points, newP)
}

func (points *PQ) Pop() interface{} {
	tmp := (*points)[len(*points)-1]
	tmp.HeapIdx = -1
	*points = (*points)[:len(*points)-1]
	return tmp
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
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	buildings := make([][]int, len(flds))
	fmt.Printf("buildings = [\n")
	for i := 0; i < len(buildings); i++ {
		buildings[i] = strToIntArray(flds[i])
		if i == 0 {
			fmt.Printf("  %s\n", intArrayToString(buildings[i]))
		} else {
			fmt.Printf(", %s\n", intArrayToString(buildings[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := getSkyline(buildings)

	timeEnd := time.Now()

	fmt.Printf("result = [\n")
	for i := 0; i < len(result); i++ {
		if i == 0 {
			fmt.Printf("  %s\n", intArrayToString(result[i]))
		} else {
			fmt.Printf(", %s\n", intArrayToString(result[i]))
		}
	}
	fmt.Printf("]\n")
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
