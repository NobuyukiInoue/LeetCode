package numarray

type NumArray struct {
	nums  []int
	n     int
	array []int
}

func Constructor(nums []int) NumArray {
	numA := new(NumArray)

	numA.n = len(nums)
	numA.nums = make([]int, len(nums))
	copy(numA.nums, nums)

	numA.array = make([]int, numA.n+1)
	for i := 0; i < numA.n; i++ {
		numA.helper(i, nums[i])
	}

	return *numA
}

func (this *NumArray) helper(i int, val int) {
	n := this.n
	i++
	for i <= n {
		this.array[i] += val
		i += i & (-i)
	}
}

func (this *NumArray) Update(i int, val int) {
	this.helper(i, val-this.nums[i])
	this.nums[i] = val
}

func (this *NumArray) SumRange(i int, j int) int {
	sumi := this.getSum(i - 1)
	sumj := this.getSum(j)
	return sumj - sumi
}

func (this *NumArray) getSum(i int) int {
	sum := 0
	i++
	for i > 0 {
		sum += this.array[i]
		i -= i & (-i)
	}

	return sum
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(i,val);
 * param_2 := obj.SumRange(i,j);
 */
