import java.util.*;

public class Solution {
    public boolean isPalindrome(String s) 
    {
        s = s.toLowerCase();
        char arr[] = s.toCharArray();
        int front = 0,back = arr.length - 1;

        while (front <= back) {
            if (((arr[front] >= 'a' && arr[front] <= 'z') || (arr[front] >= '0' && arr[front] <= '9'))) {
                if(((arr[back] >= 'a' && arr[back] <= 'z') || (arr[back] >= '0' && arr[back] <= '9'))) {
                    if(arr[front] != arr[back])
                        return false;
                    front++;
                    back--;
                } else {
                    back--;
                }
            } else {
                front++;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        boolean result = isPalindrome(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
