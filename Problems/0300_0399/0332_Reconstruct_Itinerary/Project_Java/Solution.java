import java.util.*;
import java.util.PriorityQueue;

public class Solution {
    HashMap<String, PriorityQueue<String>> map;
    
    public List<String> findItinerary(List<List<String>> tickets) {
        // 4ms
        List<String> res = new ArrayList<>();
        if(tickets == null || tickets.size() == 0)
            return res;

        map = new HashMap<>();
        for (List<String> ticket: tickets) {
            map.putIfAbsent(ticket.get(0), new PriorityQueue<String>());
            map.get(ticket.get(0)).add(ticket.get(1));
        }
        if (!map.containsKey("JFK"))
            return res;
        dfs("JFK", res);
        return res;
    }
    
    private void dfs(String start, List<String> res) {
        PriorityQueue<String> pq = map.get(start);
        while(pq != null && !pq.isEmpty()) {
            dfs(pq.poll(), res);
        }
        res.add(0, start);
    }
/*
    public List<String> findItinerary2(List<List<String>> tickets) {
        // 8ms
        Map<String, PriorityQueue<String>> targets = new HashMap<>();
        for (List<String> ticket : tickets)
            targets.computeIfAbsent(ticket.get(0), k -> new PriorityQueue()).add(ticket.get(1));
        List<String> route = new LinkedList();
        Stack<String> stack = new Stack<>();
        stack.push("JFK");
        while (!stack.empty()) {
            while (targets.containsKey(stack.peek()) && !targets.get(stack.peek()).isEmpty())
                stack.push(targets.get(stack.peek()).poll());
            route.add(0, stack.pop());
        }
        return route;
    }
*/

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] data = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<String>> tickets = ml.stringArrayToListListStringArray(data);
        System.out.println("tickets = " + ml.listListStringArrayToString(tickets));

        long start = System.currentTimeMillis();

        List<String> result = findItinerary(tickets);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
