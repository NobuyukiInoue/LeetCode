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
    private List<String> strToList(String[] data) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < data.length; i++) {
            res.add(data[i]);
        }

        return res;
    }

    private String listToString(List<String> data) {
        if (data.size() <= 0)
            return "[]";
        
        StringBuilder sb = new StringBuilder("[\"" + data.get(0) + "\"");
        for (int i = 1; i < data.size(); i++)
            sb.append(", \"" + data.get(i) + "\"");

        sb.append("]");

        return sb.toString();
    }

    private String listlistToString(List<List<String>> data) {
        if (data.size() <= 0)
            return "";

        StringBuilder sb = new StringBuilder("[" + listToString(data.get(0)));
        for (int i = 1; i < data.size(); i++)
            sb.append(", " + listToString(data.get(i)));

        sb.append("]");

        return sb.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] data = flds.split("\\],\\[");

        List<List<String>> tickets = new ArrayList<>();
            for (int i = 0; i < data.length; i++) {
            tickets.add(strToList(data[i].split(",")));
        }

        System.out.println("tickets = " + listlistToString(tickets));

        long start = System.currentTimeMillis();
        
        List<String> result = findItinerary(tickets);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + listToString(result) + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
