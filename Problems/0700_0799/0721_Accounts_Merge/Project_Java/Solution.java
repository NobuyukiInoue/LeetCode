import java.util.*;

public class Solution {
    // 24ms
    class UnionFind {
        int[] parent;
        int[] rank;
        int size;
        
        public UnionFind(int size){
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
            rank = new int[size];
            this.size = size;
        }
        
        public int find(int element){
            if (parent[element] == element) {
                return element;
            }
            return find(parent[element]);
        }
        
        public void union(int x,int y){
            int xp = find(x);
            int yp = find(y);
            if (xp == yp) {
                return;
            }
            if (rank[xp] < rank[yp]) {
                parent[xp] = yp;
            } else if (rank[yp] < rank[xp]) {
                parent[yp] = xp;
            } else {
                parent[yp] = xp;
                rank[xp]++;
            }
        }
    }

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        List<List<String>> finalList = new LinkedList<>();
        
        if (accounts.size() == 0) {
            return finalList;
        }
        
        UnionFind uF = new UnionFind(accounts.size());
        
        HashMap<String,Integer> map = new HashMap<>();
        
        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for(int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                map.putIfAbsent(email, i);
                uF.union(map.get(email), i);
            }
        }
        
        HashMap<Integer,List<String>> indexEmail = new HashMap<>();
        
        for (String email : map.keySet()) {
            int root = uF.find(map.get(email));
            indexEmail.putIfAbsent(root, new LinkedList<>());
            indexEmail.get(root).add(email);
        }
        
        for (Integer index : indexEmail.keySet()) {
            List<String> account = new LinkedList<>();
            account.add(accounts.get(index).get(0));
            
            List<String> emails = indexEmail.get(index);
            Collections.sort(emails);
            
            account.addAll(emails);
            finalList.add(account);
        }
        return finalList;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<String>> accounts = ml.stringArrayToListListStringArray(flds);
        System.out.println("accounts = " + ml.listListStringArrayToString(accounts));

        long start = System.currentTimeMillis();

        List<List<String>> result = accountsMerge(accounts);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
