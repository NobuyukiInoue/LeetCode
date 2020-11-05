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

        long start = System.currentTimeMillis();

        List<Integer> result = preorder(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
