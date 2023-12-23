package solution

import (
	"container/heap"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

// 102ms - 120ms
type Node struct {
	dist int
	x    int
	y    int
}

type PriorityQueue []Node

func (p PriorityQueue) Len() int                { return len(p) }
func (p PriorityQueue) Swap(i, j int)           { p[i], p[j] = p[j], p[i] }
func (p PriorityQueue) Less(i, j int) bool      { return p[i].dist < p[j].dist }
func (p *PriorityQueue) Push(point interface{}) { *p = append(*p, point.(Node)) }
func (p *PriorityQueue) Pop() interface{} {
	pop := (*p)[len(*p)-1]
	*p = (*p)[:len(*p)-1]
	return pop
}

func kClosest(points [][]int, K int) [][]int {
	ph, res := &PriorityQueue{}, [][]int{}
	heap.Init(ph)
	for _, p := range points {
		heap.Push(ph, Node{p[0]*p[0] + p[1]*p[1], p[0], p[1]})
	}
	for K > 0 {
		pop := heap.Pop(ph).(Node)
		res = append(res, []int{pop.x, pop.y})
		K--
	}
	return res
}

func kClosest2(points [][]int, k int) [][]int {
	// 114ms - 131ms
	for i, p := range points {
		dist := p[0]*p[0] + p[1]*p[1]
		points[i] = append(points[i], dist)
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i][2] < points[j][2]
	})

	res := [][]int{}
	for i := 0; i < k; i++ {
		res = append(res, points[i][:2])
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	flds := strings.Split(temp, "]],[")

	flds0 := strings.Split(flds[0], "],[")
	points := make([][]int, len(flds0))
	for i, _ := range flds0 {
		points[i] = StringToIntArray(flds0[i])
	}

	flds1 := strings.Replace(flds[1], "]]", "", -1)
	k, _ := strconv.Atoi(flds1)

	fmt.Printf("points = %s, k = %d\n", IntIntArrayToString(points), k)

	timeStart := time.Now()

	result := kClosest(points, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
