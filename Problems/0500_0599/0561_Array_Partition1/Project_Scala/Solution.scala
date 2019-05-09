object Solution {
    def arrayPairSum(nums: Array[Int]): Int = {
        val srt = nums.sortWith((r1, r2) => r1 < r2)
        var result = 0
        for (i <- srt.indices if i % 2 == 0)
            result += srt(i)
        result
    }

    def str_to_int_array(flds:String):Array[Int] = {
        var nums_str:Array[String] = flds.split(",")
        var nums:Array[Int] = new Array[Int](nums_str.size)

        for (i <- 0 until nums_str.length) {
            nums(i) = nums_str(i).toInt
        }

        return nums
    }

    def print_int_array(nums:Array[Int]):String = {
        if (nums.size <= 0)
            return ""

        var resultStr:String = nums(0).toString
        for (i <- 1 until nums.length) {
            resultStr += ", " + nums(i).toString
        }

        return resultStr
    }

    def main(args:String) {
        var s:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        var nums:Array[Int] = str_to_int_array(s)

        val time_start = System.currentTimeMillis
        var result:Int = arrayPairSum(nums)
        val time_end = System.currentTimeMillis

        println("result = " + result.toString)
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
