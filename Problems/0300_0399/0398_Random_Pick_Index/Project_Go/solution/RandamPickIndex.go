package solution

import "math/rand"

// 96ms

// type Solution struct {
type RandomPickIndex struct {
	nums []int
}

//func Constructor(nums []int) Solution {
func Constructor(nums []int) RandomPickIndex {
	//	return Solution{nums}
	return RandomPickIndex{nums}
}

//func (this *Solution) Pick(target int) int {
func (this *RandomPickIndex) Pick(target int) int {
	ret := -1
	randNum := -1
	for i, v := range this.nums {
		if v != target {
			continue
		}
		r := rand.Intn(1000)
		if r > randNum {
			randNum = r
			ret = i
		}
	}
	return ret
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
 */
