object Solution {
    def TwoSum(nums: Array[Int], target: Int): Array[Int] = {
        val sortedNums = nums.sorted
        var start = 0
        var end = sortedNums.size - 1
        var sum = sortedNums(start) + sortedNums(end)

        while (sum != target) {
            if(sum > target) {
                end -= 1
            } else {
                start += 1
            }
            sum = sortedNums(start) + sortedNums(end)
        }

        val elem1 = nums.indexOf(sortedNums(start))
        val elem2 = nums.lastIndexOf(sortedNums(end))
        Array(elem1, elem2)
    }
}
