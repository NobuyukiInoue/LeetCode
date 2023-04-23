public class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        // 1ms
        return (arrivalTime + delayedTime)%24;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int arrivalTime = Integer.parseInt(flds[0]);
        int delayedTime = Integer.parseInt(flds[1]);
        System.out.println("delayedTime = " + arrivalTime + ", delayedTime =  " +  + delayedTime);

        long start = System.currentTimeMillis();

        int result = findDelayedArrivalTime(arrivalTime, delayedTime);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
