import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Solution {

    public List<Integer> list = new ArrayList<>();

    public List<Integer> preorder(Node root) {
        if (root == null)
            return list;
        
        list.add(root.val);
        if (root.children == null)
            return list;
        for(Node node: root.children)
            preorder(node);
                
        return list;
    }

    /*
    public List<Integer> preorder(Node root) {
        List<Integer> list = new ArrayList<>();

        if (root == null)
            return list;
        
        list.add(root.val);

        if (root.children == null)
            return list;

        for (Node node: root.children) {
            List<Integer> temp_list = preorder(node);
            for (int i = 0; i < temp_list.size(); i++) {
                list.add(temp_list.get(i));
            }
        }
                
        return list;
    }
    */

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String json_text = args.trim().replace("$id", "val");
        ObjectMapper mapper = new ObjectMapper();
        Node root = null;

        try {
            root = mapper.readValue(json_text, Node.class);
        } catch (Exception ex) {
            System.out.println("\nmapper.readValue() Error.\n" + ex.getMessage());
            System.exit(1);
        }

        Operate_N_arr opn = new Operate_N_arr();
    //    Node root = opn.set_sample_node();
        System.out.println("root = " + opn.output_node(root));

        Mylib ml = new Mylib();

        long start = System.currentTimeMillis();

        List<Integer> result = preorder(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
