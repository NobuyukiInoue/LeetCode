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
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")
        var nums:Array[Int] = str_to_int_array(flds(0))
        var target:Int = flds(1).toInt
        println("nums = " + print_int_array(nums) + ", target = " + target)
 
        val time_start = System.currentTimeMillis

        var result: Array[Int] = TwoSum(nums, target)

        val time_end = System.currentTimeMillis

        println("result = " + print_int_array(result) )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
