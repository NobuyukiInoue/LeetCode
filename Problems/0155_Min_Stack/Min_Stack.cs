using System;

public class MinStack {

    private int[] stack = new int[65535];
    private int index = 0;

    /** initialize your data structure here. */
    public MinStack() {
    }
    
    public void Push(int x) {
        stack[index++] = x;
        Console.WriteLine("Push(" + x.ToString() + ");");
    }
    
    public void Pop() {
        --index;
        Console.WriteLine("Pop();");
    }
    
    public int Top() {
        return stack[index - 1];
        Console.WriteLine("Top();");
    }
    
    public int GetMin() {
        int min_val = stack[index - 1];

        for (int i = 0; i < index - 1; ++i){
            if (stack[i] < min_val) {
                min_val = stack[i];
            }
        }

        Console.WriteLine("GetMin() => " + min_val.ToString());
        return min_val;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
public class Solution
{
    private void calc()
    {
        MinStack minStack = new MinStack();
        minStack.Push(-2);
        minStack.Push(0);
        minStack.Push(-3);
        minStack.GetMin();
        minStack.Pop();
        minStack.Top();
        minStack.GetMin();
    }

    public void Main(string args)
    {
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        calc();

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
