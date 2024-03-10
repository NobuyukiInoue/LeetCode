import java.util.*;

public class Solution {
    public int numRescueBoats(int[] people, int limit) {
        // 16ms - 18ms
        Arrays.sort(people);
        int ans = 0, i = 0, j = people.length - 1;
        while (i <= j) {
            ans++;
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] people = ml.stringToIntArray(flds[0]);
        int limit = Integer.parseInt(flds[1]);
        System.out.println("people = " + ml.intArrayToString(people) + ", limit = " + limit);

        long start = System.currentTimeMillis();

        int result = numRescueBoats(people, limit);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
