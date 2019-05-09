object Solution {
    def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
        var all_nums:Array[Int] = Array.concat(nums1, nums2).sorted
        if (all_nums.length % 2 == 1)
            return all_nums(all_nums.length/2);
        else
            return (all_nums(all_nums.length/2 - 1) + all_nums(all_nums.length/2))/2.0;
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
        var nums1:Array[Int] = str_to_int_array(flds(0))
        var nums2:Array[Int] = str_to_int_array(flds(1))

        val time_start = System.currentTimeMillis

        var result:Double = findMedianSortedArrays(nums1, nums2)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString)
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
