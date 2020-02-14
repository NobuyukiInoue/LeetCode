package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func smallestStringWithSwaps(s string, pairs [][]int) string {
	// 120ms
	n := len(s)
	uf := newUnionFind(n)

	for _, p := range pairs {
		uf.connect(p[0], p[1])
	}

	groups := make(map[int][]int, n)
	for c, p := range uf.parent {
		p = uf.find(p)
		groups[p] = append(groups[p], c)
	}

	bytes := []byte(s)
	res := make([]byte, n)
	for _, g := range groups {
		size := len(g)
		t := make([]int, size)
		copy(t, g)
		if size > 1 {
			sort.Slice(t, func(i, j int) bool {
				return bytes[t[i]] < bytes[t[j]]
			})
			sort.Ints(g)
		}
		for i := 0; i < size; i++ {
			res[g[i]] = bytes[t[i]]
		}
	}

	return string(res)
}

type unionFind struct {
	parent []int
}

func newUnionFind(size int) *unionFind {
	parent := make([]int, size)
	for i := range parent {
		parent[i] = i
	}
	return &unionFind{
		parent: parent,
	}
}

func (uf *unionFind) connect(x, y int) {
	uf.parent[uf.find(x)] = uf.find(y)
}

func (uf *unionFind) find(i int) int {
	if uf.parent[i] != i {
		uf.parent[i] = uf.find(uf.parent[i])
	}
	return uf.parent[i]
}

func strToIntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func printIntArray(nums []int) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.Itoa(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.Itoa(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	s := strings.Replace(flds[0], "[", "", -1)
	fmt.Printf("s = %s\n", s)

	data := strings.Split(flds[1], "],[")
	pairs := make([][]int, len(data))
	for i := 0; i < len(data); i++ {
		pairs[i] = strToIntArray(data[i])
	}

	fmt.Printf("pairs = [")
	for i, _ := range pairs {
		if i == 0 {
			fmt.Printf("[%s]", printIntArray(pairs[i]))
		} else {
			fmt.Printf(",[%s]", printIntArray(pairs[i]))
		}
	}
	fmt.Printf("]\n")

	timeStart := time.Now()

	result := smallestStringWithSwaps(s, pairs)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
