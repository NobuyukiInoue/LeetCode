public class Solution {
    public bool IsPalindrome(int x) {
        string temp = x.ToString();
        
        for (int i = 0; i < temp.Length / 2; i++) {
            if (temp[i] != temp[temp.Length - 1 - i])
                return false;
        }
        
        return true;
    }
}
