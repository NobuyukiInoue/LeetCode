import scala.math.{max}

object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        var largestLength:Int = 0
        var currLength:Int = 1
        var start:Int = 0

        for (i <- 0 until s.size) {
            var found:Int = s.substring(start, start + currLength).indexOf(s(i));
            if (found != (i - start) && found != -1)
            {
                var subtractionLength:Int = found + 1;
                currLength = currLength - subtractionLength;
                start += subtractionLength;
            }
            
            if (currLength > largestLength)
            {
                largestLength = currLength;
            }

            currLength += 1
        }
        
        return largestLength
    }

    def lengthOfLongestSubstring_functionalStyle(s: String): Int = {
        if (s.isEmpty) 0
        val resultMap = s.zipWithIndex.foldLeft(Map[String, Int]("max" -> 0, "last" -> -1))((map, pair) => {
            if (map.getOrElse("" + pair._1, -1) > map.getOrElse("last", -1)) 
                map + ("last" -> map.getOrElse("" + pair._1, -1),
                      ("" + pair._1) -> pair._2)
            else {
                map + ("" + pair._1 -> pair._2, "max" -> max(map.getOrElse("max", 0), pair._2 - map.getOrElse("last", -1)))
            }
        })
        resultMap.getOrElse("max", 0)
    }

    def main(args:String): Unit = {
        var s:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        println("s = " + s )
 
        val time_start = System.currentTimeMillis

        var result:Int = lengthOfLongestSubstring(s)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
