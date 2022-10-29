import java.util.*;
import java.util.stream.*;

public class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // 12ms - 15ms
        Map<Integer, String> map = new HashMap<>();
        for (int i = 0; i < names.length; i++) {
            map.put(heights[i], names[i]);
        }        
        Arrays.sort(heights);
        String[] result = new String[heights.length];
        int index = 0;
        for (int i = heights.length - 1; i >= 0; i--) {
            result[index] = map.get(heights[i]);
            index++;
        }
        return result;
    }
    /*
    // 26ms
    private record Person(String name, int height) {}

    public String[] sortPeople(String[] names, int[] heights) {
        var people = IntStream.range(0, names.length)
                              .mapToObj(i -> new Person(names[i], heights[i]))
                              .toArray(Person[]::new);
                              
        Arrays.sort(people, Comparator.comparingInt(p -> -p.height));
        IntStream.range(0, names.length)
                 .forEach(i -> names[i] = people[i].name);
        return names;
    }
    */

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] heights = Mylib.stringToIntArray(flds[1]); 
        String[] names = flds[0].split(",");
        System.out.println("names = " + ml.stringArrayToString(names) + ", heights = " + ml.intArrayToString(heights));

        long start = System.currentTimeMillis();

        String[] result = sortPeople(names, heights);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + ml.stringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
