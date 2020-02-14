import java.util.*;

public class Solution {

    public List<List<String>> findDuplicate(String[] paths) {
        // 22ms
        List<List<String>> tr = new ArrayList<>();
        Map<String, List<String>> data = new HashMap<>();
        
        for (String chunk: paths) {
            String[] chunks = chunk.split(" ");
            String basePath = chunks[0];
            
            for (int i=1;i<chunks.length;i++) {
                String file = chunks[i];
                String filename = file.substring(0, file.indexOf('('));
                String fullPath = basePath + "/" + filename;
                String contents = file.substring(file.indexOf('('));
                
                if (!data.containsKey(contents)) {
                    data.put(contents, new ArrayList<String>());
                }
                data.get(contents).add(fullPath);
            }
        }
        
        for (String contents: data.keySet()) {
            if (data.get(contents).size() < 2) continue;
            List<String> all = new ArrayList<>();
            for (String path: data.get(contents)) {
                all.add(path);
            }
            tr.add(all);
        }
        
        return tr;
    }

    public List<List<String>> findDuplicate2(String[] paths) {
        // 47ms
        List<List<String>> result = new ArrayList<List<String>>();
        int n = paths.length;
        if (n == 0)
            return result;
        
        Map<String, Set<String>> map = new HashMap<>();
        for (String path : paths) {
            String[] strs = path.split("\\s+");
            for (int i = 1; i < strs.length; i++) {
                int idx = strs[i].indexOf("(");
                String content = strs[i].substring(idx);
                String filename = strs[0] + "/" + strs[i].substring(0, idx);
                Set<String> filenames = map.getOrDefault(content, new HashSet<String>());
                filenames.add(filename);
                map.put(content, filenames);
            }
        }
        
        for (String key : map.keySet()) {
            if (map.get(key).size() > 1) {
                result.add(new ArrayList<String>(map.get(key)));
            }
        }
        
        return result;
    }

    private String stringArrayToString(String[] arr) {
        if (arr.length <= 0)
            return "";
        StringBuffer sb = new StringBuffer("[" + arr[0]);
        for (int i = 1; i < arr.length; i++) {
            sb.append(", " + arr[i]);
        }
        sb.append("]");
        return sb.toString();
    }

    private String listlistArrayToString(List<List<String>> arr) {
        if (arr.size() <= 0)
            return "";
        StringBuffer sb = new StringBuffer("[" + listArrayToString(arr.get(0)));
        for (int i = 1; i < arr.size(); i++) {
            sb.append(", " + listArrayToString(arr.get(i)));
        }
        sb.append("]");
        return sb.toString();
    }


    private String listArrayToString(List<String> arr) {
        if (arr.size() <= 0)
            return "";
        StringBuffer sb = new StringBuffer("[" + arr.get(0));
        for (int i = 1; i < arr.size(); i++) {
            sb.append(", " + arr.get(i));
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] paths = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        System.out.print("paths = " + stringArrayToString(paths));

        long start = System.currentTimeMillis();
        
        List<List<String>> result = findDuplicate(paths);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listlistArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
