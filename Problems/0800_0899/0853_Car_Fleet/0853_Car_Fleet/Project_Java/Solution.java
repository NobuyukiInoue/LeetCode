import java.util.*;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // 9ms
        if (position.length < 1 || speed.length < 1)
            return 0;
        HashMap<Integer, Integer> posToSpeed = new HashMap<Integer, Integer>();
        for (int i = 0; i < position.length; i++)
            posToSpeed.put(position[i], speed[i]);
        Arrays.sort(position);
        
        float leaderTime = (float)(target-position[position.length - 1])/posToSpeed.get(position[position.length - 1]);
        int currGroups = 1;
        for (int i = position.length - 2; i >= 0; i--) {
            float currTime = (float)(target - position[i]) / posToSpeed.get(position[i]);
            if (currTime > leaderTime) {
                currGroups++;
                leaderTime = currTime;
            }
        }
        
        return currGroups;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int target = Integer.parseInt(flds[0].replace("[[", ""));
        int[] position;
        if (flds.length > 1) {
            position = ml.stringToIntArray(flds[1]);
        } else {
            position = new int[0];
        }

        int[] speed;
        if (flds.length > 2) {
            String flds2 = flds[2].replace("]]", "");
            speed = ml.stringToIntArray(flds2);
        } else {
            speed = new int[0];
        }

        System.out.println("target = " + Integer.toString(target)
                         + ", position = " + ml.intArrayToString(position)
                         + ", speed = " + ml.intArrayToString(speed));

        long start = System.currentTimeMillis();

        int result = carFleet(target, position, speed);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
