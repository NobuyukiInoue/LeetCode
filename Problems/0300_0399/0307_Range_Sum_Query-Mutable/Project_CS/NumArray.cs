public class NumArray {
    int[] nums;
    int n;
    int[] array;

    public NumArray(int[] nums)
    {
        this.nums = nums;
        this.n = nums.Length;
        this.array = new int[this.n + 1];
        for (int i = 0; i < n; i++) {
            this.helper(i, nums[i]);
        }
    }

    private void helper(int i, int val)
    {
        int n = this.n;
        i++;
        while (i <= n)
        {
            this.array[i] += val;
            i += i & (-i);
        }
    }

    public void Update(int i, int val)
    {
        this.helper(i, val - this.nums[i]);
        this.nums[i] = val;
    }

    public int SumRange(int i, int j)
    {
        int sum_i = this.get_sum(i - 1);
        int sum_j = this.get_sum(j);
        
        return sum_j - sum_i;
    }

    private int get_sum(int i)
    {
        int sum = 0;
        i++;
        while (i > 0)
        {
            sum += this.array[i];
            i -= i & (-i);
        }
        
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.Update(i,val);
 * int param_2 = obj.SumRange(i,j);
 */
