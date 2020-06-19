public class Solution {
    private void BSTIteratorMain(String[] cmds, TreeNode mynode) {
        BSTIterator BI = new BSTIterator(mynode);
        boolean isExistBI = false;

        for (String cmd :cmds) {
            if (cmd.equals("BSTIterator")) {
                // BI = new BSTIterator(mynode);
                System.out.println("BSTIterator iterator = new BSTIterator(root);");
                isExistBI = true;
            } else if (cmd.equals("next") && isExistBI) {
                System.out.println("iterator.next();\t ... " + Integer.toString(BI.next()));
            } else if (cmd.equals("hasNext") && isExistBI) {
                System.out.println("iterator.hasNext();\t ... " + Boolean.toString(BI.hasNext()));
            }
        }
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"","").replace(", ",",").trim().split("\\],\\[\\[\\[");

        String[] cmds = flds[0].replace("[[", "").split(",");

        String node_flds = (flds[1].split("\\]\\],\\["))[0];
        OperateTreeNode ope_t = new OperateTreeNode();
    //  Codec codec = new Codec();
        TreeNode mynode;
        
        if (node_flds.length() > 0) {
            mynode = ope_t.createTreeNode(node_flds);
        //  mynode = codec.deserialize(node_flds);
        } else {
            mynode = null;
        }

        System.out.print("mynode = \n" + ope_t.treeToStaircaseString(mynode));
        System.out.println("mynode = " + ope_t.tree2str(mynode));

        long start = System.currentTimeMillis();

        BSTIteratorMain(cmds, mynode);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
