import java.util.*;

public class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        // 52ms
        int n = s.length();
        int[] root = new int[n];

        for (int i = 0; i < n; ++i)
            root[i] = i;

        for (List<Integer> p : pairs)
            union(root, p.get(0), p.get(1));

        Map<Integer, PriorityQueue<Character>> map = new HashMap<Integer, PriorityQueue<Character>>();
        for (int i = 0; i < n; ++i) {
            int head = findRoot(root, i);
            root[i] = head;
            if (!map.containsKey(head)) map.put(head, new PriorityQueue<Character>());
            map.get(head).add(s.charAt(i));
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; ++i)
            sb.append(map.get(root[i]).poll());

        return sb.toString();
    }
    
    private int findRoot(int[] root, int i) {
        if (root[i] == i)
            return i;
        int r = findRoot(root, root[i]);
        root[i] = r;
        return r;
    }
    
    private void union(int[] root, int src, int dst) {
        int srcRoot = findRoot(root, src);
        int dstRoot = findRoot(root, dst);
        if (srcRoot != dstRoot)
            root[srcRoot] = dstRoot;
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("]]]", "").trim().split("\\],\\[\\[");

        String s = flds[0].replace("[", "");
        System.out.println("s = " + s);

        Mylib ml = new Mylib();
        String[] data = flds[1].split("\\],\\[");
        List<List<Integer>> pairs = new ArrayList<List<Integer>>();
    
        for (int i = 0; i < data.length; i++) {
            String[] cols = data[i].split(",");
            List<Integer> l_cols = new ArrayList<Integer>();
            l_cols.add(Integer.parseInt(cols[0]));
            l_cols.add(Integer.parseInt(cols[1]));
            pairs.add(l_cols);
        }

        System.out.print("pairs = [");
        for (int i = 0; i < pairs.size(); i++) {
            if (i == 0)
                System.out.print(listArrayToString(pairs.get(i)));
            else
                System.out.print("," + listArrayToString(pairs.get(i)));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        String result = smallestStringWithSwaps(s, pairs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
