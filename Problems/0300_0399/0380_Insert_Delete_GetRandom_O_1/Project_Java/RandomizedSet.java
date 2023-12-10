import java.util.*;

// 21ms - 26ms
class RandomizedSet {
    HashMap<Integer, Integer> data_map;
    List<Integer> data;
    Random rand;

    public RandomizedSet() {
        data_map = new HashMap<>();
        data = new ArrayList<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (!data_map.containsKey(val)) {
            data.add(val);
            data_map.put(val, data.size() - 1);
            return true;
        }
        return false;
    }
    
    public boolean remove(int val) {
        if (data_map.containsKey(val)) {
            int index = data_map.remove(val);
            int lastVal = data.remove(data.size() - 1);
            if (lastVal != val) {
                data.set(index, lastVal);
                data_map.put(lastVal, index);
            }
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        return data.get(rand.nextInt(data.size()));
    }
}

/*
public int[] shuffle() {
    Random rand = new Random();
    int[] ans = arr.clone();
    for (int i = 0; i < ans.length; i++) {
        int swp_num = rand.nextInt(ans.length);
        int temp = ans[i];
        ans[i] = ans[swp_num];
        ans[swp_num] = temp;
    }
    return ans;
}
*/

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
 