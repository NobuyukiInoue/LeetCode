package solution

import (
	"math/rand"
	"time"
)

// 13ms - 23ms
type Solution2 struct {
	arr []int
}

func Constructor(nums []int) Solution2 {
	rand.Seed(time.Now().UnixNano())
	return Solution2{nums}
}

func (this *Solution2) Reset() []int {
	return this.arr
}

func (this *Solution2) Shuffle() []int {
	arr := make([]int, len(this.arr))
	copy(arr, this.arr)
	for i := 0; i < len(arr)-1; i++ {
		swp_num := rand.Intn(len(arr) - i)
		arr[len(arr)-1-i], arr[swp_num] = arr[swp_num], arr[len(arr)-1-i]
	}
	return arr
}

/*
// Wrong answer 7/8

type Solution struct {
	arr []int
}

func Constructor(nums []int) Solution {
	rand.Seed(time.Now().UnixNano())
	return Solution{nums}
}

func (this *Solution) Reset() []int {
	return this.arr
}

func (this *Solution) Shuffle() []int {
	n := len(this.arr)

	arr := make([]int, len(this.arr))
	copy(arr, this.arr)

	for i := 0; i < n; i++ {
		swp_num := rand.Intn(n)
		arr[0], arr[swp_num] = arr[swp_num], arr[0]
	}
	return arr
}
*/

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
