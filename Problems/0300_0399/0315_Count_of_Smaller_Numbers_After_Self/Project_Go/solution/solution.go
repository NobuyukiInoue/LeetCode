package solution

import (
	"fmt"
	"strings"
	"time"
)

import "sort"

type BinaryIndexTree struct {
	nodes []int
}

func newBinaryIndexTree(length int) *BinaryIndexTree {
	// Length of BIT must be 1 bigger than the actual length
	// to work with the bit manp magic
	return &BinaryIndexTree{nodes: make([]int, length + 1)} 
}

// Sums all existing values less than this index
func (this *BinaryIndexTree) sum(index int) int {
	// convert to BIT indexing
	index++
	sum := 0
	for index > 0 {
		sum += this.nodes[index]

		// bit manpulation, iterates up the BIT
		index = index - index&(-index)
	}
    return sum
}

// Adds index into BIT for future sum queries
func (this *BinaryIndexTree) add(index int) {
	// convert to BIT indexing
	index++

	for index < len(this.nodes) {
		this.nodes[index]++

		// bit mapulation, increment count for all 
		// greater powers of 2 within BIT length
		index = index + index&(-index)
	}

}

func countSmaller(nums []int) []int {
	length := len(nums)
	sortedNums := append([]int{}, nums...)
	sort.Ints(sortedNums)

	hash := make(map[int]int)
	lowerCount := 0
	for _, num := range sortedNums {
        if _, ok := hash[num]; !ok {
			hash[num] = lowerCount
			lowerCount++
		}
	}

	BIT := newBinaryIndexTree(length)
	result := make([]int, length)

	for i := length - 1; i >= 0; i-- {
		count := hash[nums[i]]
		
		// Sum existing nodes less than this count
		result[i] = BIT.sum(count - 1)
		
		// Add count
		BIT.add(count)
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := countSmaller(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
