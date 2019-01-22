object Solution {
    def checkRecord(s: String): Boolean = {
        return !(s.indexOf("A") != s.lastIndexOf("A") || s.contains("LLL"));        
    }
}
