import scala.io.Source

object Main {
    def output_List(list:List[String]): String = {
        if (list.size <= 0)
            return ""
        
        var resultStr:String = "\"" + list(0) + "\"" 
        for (i <- 0 until list.size) {
            resultStr += ", \"" + list(i) + "\""
        }

        return resultStr
    }

    def loop_main(args:String) {
        var digits:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        println("digits = " + digits)
 
        val time_start = System.currentTimeMillis

        var result:List[String] = Solution.letterCombinations(digits)

        val time_end = System.currentTimeMillis

        println("result = " + output_List(result))
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
