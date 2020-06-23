import scala.collection.mutable

object Solution {
    def letterCombinations(digits: String): List[String] = {
        // Corner case.
        if (digits.size == 0) {
            return List[String]()
        }
        
        // Map a digit to the letters it could represent.
        val numToLetters = Map('2' -> "abc", '3' -> "def", '4' -> "ghi", '5' -> "jkl", 
                               '6' -> "mno", '7' -> "pqrs", '8' -> "tuv", '9' -> "wxyz")
        
        // Nested method to transfer digits given to a list of corresponding letters.
        val letterList = getLetterList(digits, numToLetters)
        var finalResult = new scala.collection.mutable.ArrayBuffer[String]()
        letterCombinationsAfter(letterList, "", finalResult)
        
        finalResult.toList
    }

    def getLetterList(digits: String, numToLetters:Map[Char, String]): List[String] = {
        var letterArrayBuffer = new scala.collection.mutable.ArrayBuffer[String]()
        for (i <- 0 until digits.length) {
            letterArrayBuffer += numToLetters(digits(i))
        }
        letterArrayBuffer.toList
    }

    def letterCombinationsAfter(letterList: List[String], curComb: String, finalResult: scala.collection.mutable.ArrayBuffer[String]): Unit = {
        if (curComb.length == letterList.size) {
            finalResult += curComb
            return
        }
        
        var letters = letterList(curComb.length)
        for (i <- 0 until letters.length) {
            letterCombinationsAfter(letterList, curComb + letters(i), finalResult)
        }        
    }

    def output_List(list:List[String]): String = {
        if (list.size <= 0)
            return ""
        
        var resultStr:String = "\"" + list(0) + "\"" 
        for (i <- 0 until list.size) {
            resultStr += ", \"" + list(i) + "\""
        }

        return resultStr
    }

    def main(args:String): Unit = {
        var digits:String = args.stripLineEnd.replaceAll(" ", "").replaceAll("\"", "").replaceFirst("\\[", "").replaceFirst("\\]", "")
        println("digits = " + digits)
 
        val time_start = System.currentTimeMillis

        var result:List[String] = letterCombinations(digits)

        val time_end = System.currentTimeMillis

        println("result = " + output_List(result))
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
