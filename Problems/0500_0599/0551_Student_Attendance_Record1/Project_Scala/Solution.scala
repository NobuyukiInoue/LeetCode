object Solution {
    def checkRecord(s: String): Boolean = {
        return !(s.indexOf("A") != s.lastIndexOf("A") || s.contains("LLL"));
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

    def main(args:String): Unit = {
        var s:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        println(s)

        val time_start = System.currentTimeMillis

        var result:Boolean = checkRecord(s)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString)
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
