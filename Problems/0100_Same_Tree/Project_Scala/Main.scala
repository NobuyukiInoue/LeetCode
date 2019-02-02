import java.io.File
import scala.io.Source

object Main {
    def main(args:Array[String]) {
        var className:String = new Object(){}.getClass().getEnclosingClass().getName()

        if (args.size < 1) {
            println("Usage)\n" +
                    "scala " + className.diff("$") + " <testdataFile>\n")
            sys.exit()
        }

        if (new File(args(0)).exists() == false) {
            println(args(0) + " not found.")
            sys.exit()
        }

        val s = Source.fromFile(args(0))

        try {
            for (line <- s.getLines) {
                var trimmed_line:String = line.trim
                if (trimmed_line != "") {
                    println("args = " + trimmed_line)
                    Solution.main(trimmed_line)
                }
            }
        } finally {
            s.close
        }
    }
}
