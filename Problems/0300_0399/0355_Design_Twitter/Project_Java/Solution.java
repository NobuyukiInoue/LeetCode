import java.util.*;

public class Solution {
    public void execTwitter(String[] cmds, List<List<Integer>> args) {
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
                    System.out.println("getNewsFeed(" + Integer.toString(args.get(i).get(0)) + ") ... " + listArrayToString(result));

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

    public String StringArray2String(String[] data) {
        if (data.length <= 0)
            return "";

        String resultStr;
        if (data[0].length() == 0) {
            resultStr = "null";
        } else {
            resultStr = data[0];
        }

        for (int i = 1; i < data.length; i++) {
            if (data[i].length() == 0) {
                resultStr += ", null";
            } else {
                resultStr += ", " + data[i];
            }

        }

        return resultStr;
    }

    public String listListArrayToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + listArrayToString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + listArrayToString(list.get(i));
        }

        return resultStr + "]";
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
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] strVals = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> args = new ArrayList<List<Integer>>();

        for (int i = 0; i < strVals.length; i++) {
            List<Integer> tempList = new ArrayList<Integer>();

            if (strVals[i].length() != 0) {
                int[] flds2 = ml.stringTointArray(strVals[i]);
                for (int j = 0; j < flds2.length; j++) {
                    tempList.add(flds2[j]);
                }
            }
            args.add(tempList);
        }

        System.out.println("cmds[] = " + StringArray2String(cmds));
        System.out.println("args[] = " + listListArrayToString(args));

        long start = System.currentTimeMillis();

        execTwitter(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
