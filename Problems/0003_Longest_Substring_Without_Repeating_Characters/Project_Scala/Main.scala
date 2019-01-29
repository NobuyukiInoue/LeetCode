import scala.io.Source

object Main {
    def loop_main(args:String) {
        var s:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        println("s = " + s )
 
        val time_start = System.currentTimeMillis

        var result:Int = Solution.lengthOfLongestSubstring(s)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }

    def main(args:Array[String]) {
        var className:String = new Object(){}.getClass().getEnclosingClass().getName()

        if (args.size < 1) {
            println("Usage)\n" +
                    "scala " + className.diff("$") + " <testdataFile>\n")
            sys.exit()
        }

        val s = Source.fromFile(args(0))
        try {
            for (line <- s.getLines) {
                println("args = " + line)
                loop_main(line)
            }
        } finally {
            s.close
        }
    }
}
