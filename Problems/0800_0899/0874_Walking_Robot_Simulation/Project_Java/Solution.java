import java.util.*;

public class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        Set<String> obstaclesRowToCols = new HashSet<>();
        for (int[] obstacle : obstacles) {
            obstaclesRowToCols.add(obstacle[0] + " " + obstacle[1]);
        }

        int x = 0, y = 0, direction = 1, maxDistSquare = 0;
        for (int i = 0; i < commands.length; i++) {
            if (commands[i] == -2) {
                direction--;
                if (direction < 0) {
                    direction += 4;
                }
            } else if (commands[i] == -1) {
                direction++;
                direction %= 4;
            } else {
                int step = 0;
                while (step < commands[i] && (!obstaclesRowToCols.contains((x + directions[direction][0]) + " " + (y + directions[direction][1])))) {
                    x += directions[direction][0];
                    y += directions[direction][1];
                    step++;
                }
            }
            maxDistSquare = Math.max(maxDistSquare, x * x + y * y);
        }

        return maxDistSquare;
    }

    public int robotSim2(int[] commands, int[][] obstacles) {
        // 1282ms
        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int x = 0, y = 0, direction = 1, maxDistSquare = 0;
        for (int i = 0; i < commands.length; i++) {
            if (commands[i] == -2) {
                direction--;
                if (direction < 0) {
                    direction += 4;
                }
            } else if (commands[i] == -1) {
                direction++;
                direction %= 4;
            } else {
                int step = 0;
                while (step < commands[i] && !(PostionHit(obstacles, x + directions[direction][0], y + directions[direction][1]))) {
                    x += directions[direction][0];
                    y += directions[direction][1];
                    step++;
                }
            }
            maxDistSquare = Math.max(maxDistSquare, x * x + y * y);
        }

        return maxDistSquare;
    }

    private boolean PostionHit(int[][] obstacles, int x, int y) {
        for (int i = 0; i < obstacles.length; i++) {
            if (obstacles[i][0] == x)
                if (obstacles[i][1] == y)
                    return true;
        }

        return false;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] str_args = args.replace("\"", "").replace(" ", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();

        int[] commands = ml.stringToIntArray(str_args[0].replace("[[",""));
        System.out.println("commands = " + ml.intArrayToString(commands));

        String[] str_obstacles = str_args[1].replace("]]]", "").split("\\],\\[");

        int[][] obstacles;
        if (str_obstacles[0].equals("") == false) {
            obstacles= ml.stringToIntIntArray(str_obstacles);
            System.out.println("obstacles = " + ml.intIntArrayToString(obstacles));
        } else {
            obstacles = new int[0][0];
            System.out.println("[[]]");
        }

        long start = System.currentTimeMillis();

        int result = robotSim(commands, obstacles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
