object Solution {
    def arrayPairSum(nums: Array[Int]): Int = {
        val srt = nums.sortWith((r1, r2) => r1 < r2)
        var result = 0
        for (i <- srt.indices if i % 2 == 0)
            result += srt(i)
        result
    }
}
