import java.util.*;

public class Solution {
    public void execTwitter(String[] cmds, List<List<Integer>> args) {
        Mylib ml = new Mylib();
        Boolean createdTwitter = false;
        Twitter twitter = new Twitter();

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("Twitter")) {
                createdTwitter = true;
            } else {
                if (createdTwitter != true) {
                    System.out.println("Twitter() is not executed.");
                    System.exit(1);

                } else if (cmds[i].equals("postTweet")) {
                    twitter.postTweet(args.get(i).get(0), args.get(i).get(1));
                    System.out.println("postTweet(" + Integer.toString(args.get(i).get(0)) + ", " +  Integer.toString(args.get(i).get(1)) + ")");

                } else if (cmds[i].equals("getNewsFeed")) {
                    List<Integer> result = twitter.getNewsFeed(args.get(i).get(0));
                    System.out.println("getNewsFeed(" + Integer.toString(args.get(i).get(0)) + ") ... " + ml.listIntArrayToString(result));

                } else if (cmds[i].equals("follow")) {
                    twitter.follow(args.get(i).get(0), args.get(i).get(1));
                    System.out.println("follow(" + Integer.toString(args.get(i).get(0)) + ", " + Integer.toString(args.get(i).get(1)) + ")");

                } else if (cmds[i].equals("unfollow")) {
                    twitter.unfollow(args.get(i).get(0), args.get(i).get(1));
                    System.out.println("unfollow(" + Integer.toString(args.get(i).get(0)) + ", " + Integer.toString(args.get(i).get(1)) + ")");

                }
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] strVals = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> args = new ArrayList<List<Integer>>();

        for (int i = 0; i < strVals.length; i++) {
            List<Integer> tempList = new ArrayList<Integer>();

            if (strVals[i].length() != 0) {
                int[] flds2 = ml.stringToIntArray(strVals[i]);
                for (int j = 0; j < flds2.length; j++) {
                    tempList.add(flds2[j]);
                }
            }
            args.add(tempList);
        }

        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.listListIntArrayToString(args));

        long start = System.currentTimeMillis();

        execTwitter(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
