import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Solution {

    public List<Integer> postorder(Node root) {
        List<Integer> result = new LinkedList<>();
        Stack<Node> nodeStack = new Stack<>();
        if (root == null) {
            return result;
        }
        
        nodeStack.push(root);
        
        while (!nodeStack.isEmpty()) {
            Node nextNode = nodeStack.pop();
            result.add(0, nextNode.val);
            
            for (Node node : nextNode.children) {
                if (node != null) {
                    nodeStack.push(node);
                }
            }
        }
        return result;
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

        long start = System.currentTimeMillis();

        List<Integer> result = postorder(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
